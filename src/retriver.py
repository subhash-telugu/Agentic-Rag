from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.tools.retriever import create_retriever_tool



class DataEmbedding:
    """Retriever class to load and split PDF files."""
    def __init__(self,chunk_size=1000, chunk_overlap=200):   
            self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
            self.vectorstore = None
            self.retriever = None

    def get_retriever(self,path,model="sentence-transformers/all-MiniLM-L6-v2"):
        """Load the PDF file and split it into chunks."""
        loader=PyPDFLoader(path)
        documents=loader.load()
        
        texts=self.text_splitter.split_documents(documents)      
        embeddings=HuggingFaceEmbeddings(model_name=model)
        self.vectorstore=FAISS.from_documents(texts,embeddings)
        self.retriever= self.vectorstore.as_retriever(k=2)
    def get_tool(self):
         retriever_tool=create_retriever_tool(
            self.retriever,
            "retriever_vector_db_blog",
            "Search and run information about Langgraph"
         )
         return retriever_tool