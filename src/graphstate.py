from pydantic import BaseModel, Field
from typing import TypedDict
from langchain_core.messages import BaseMessage
from typing import Annotated,Sequence

from langgraph.graph.message import add_messages

class State(TypedDict):
    """State class to represent the state of the application.

    
    """
    query: str = Field(..., description="The query to be processed")
    updated_query: str = Field(..., description="The updated value of the query")
    output: str = Field(..., description="The value of the state")
    messages: Annotated[Sequence[BaseMessage], add_messages]
    grade:str
    generated_out:str
   