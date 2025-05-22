from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os   

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

def get_llm():
    """Get the LLM instance."""
    # Initialize the LLM with the desired model
    llm=ChatGroq(model='llama-3.3-70b-versatile')

    return llm

