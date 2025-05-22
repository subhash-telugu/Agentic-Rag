from pydantic import Field,BaseModel
from src.llmUtils.llm import get_llm
from typing import Literal
from src.graphstate import State
from langchain.prompts import PromptTemplate
from langchain_core.messages import HumanMessage
class Grade(BaseModel):
    """score for relevance check."""

    binary_score:str = Field(description="Relevance score 'generate' or 'rewrite'")


def grader(state:State):
    llm=get_llm()
    prompt = PromptTemplate(
    template="""You are a grader assessing relevance of a retrieved document to a user question. \n 
    Here is the retrieved document: \n\n {context} \n\n
    Here is the user question: {question} \n
    If the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant and can be approved for generation if it is rejected it goes for rewrite \n
    Give a score 'generate' or 'rewrite' score to indicate whether the document is relevant to the question.
    only mention it should be rewrite or to generate
    ouput:'genereate' or 'rewrite' '""",
    input_variables=["context", "question"],
    )
    
    llm=llm.with_structured_output(Grade)
    query=state['query']
    chain=prompt|llm
    tool_meesage=state['messages'][-1]
    try:
       
       out=chain.invoke({"context":tool_meesage,'question':query})
       print('no error')
    except:
        print('error in grade')
        
    return out.binary_score

