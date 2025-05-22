from src.llmUtils.llm import get_llm
from src.graphstate import State
from langchain_core.messages import HumanMessage


class ToolCall:
    def __init__(self, retriever_tool):
        self.retriever_tool = retriever_tool

    def call(self,state:State):
        """ Invokes the agent model to generate a response based on the current state. Given
        the question, it will decide to retrieve using the retriever tool, or simply end.
        get the response only from tool

        Args:
            state (query): The current state

        Returns:
            dict: The updated state with the agent response 
        """     
        # Initialize the LLM with the retriever tool
        llm = get_llm()
        llm_tool = llm.bind_tools([self.retriever_tool])
        print("llm responded with tool call")
     
        # Create a HumanMessage with the query
        message = [HumanMessage(content=state['query'])]
      
        # Invoke the LLM with the message
        response = llm_tool.invoke(message)
        print("agent responded")
        return {'messages':[response]}