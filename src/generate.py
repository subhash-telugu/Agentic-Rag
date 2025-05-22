from src.llmUtils.llm import get_llm
from src.graphstate import State

from langchain.prompts import PromptTemplate

from langchain_core.output_parsers import StrOutputParser

def generator(state:State):

    llm = get_llm() 
    print("LLM initialized successfully")
  

   

    template="""Answer the following based on the following context.
    think step by step before providing a detailed answer
    <context>
    {context}
    </context>
    Question: {input}"""
    Prompt = PromptTemplate( 
        input_variables=["context", "input"],
        template=template
    )
    print("generated the output")   
    
    chain =Prompt | llm 
    query=state['query']
    tool_meesage=state['messages'][-1]
     
    out=chain.invoke({"context":tool_meesage,'input':query})
    return {'generated_out':out.content}


