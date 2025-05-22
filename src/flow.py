from langgraph.graph import StateGraph,START,END
from src.graphstate import State
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition
from src.agent import ToolCall
from src.grade import grader
from src.generate import generator
from src.rewrite import rewrite

# from src.condition import tools_condition

class ModelGraph:
    """ModelGraph class to initialize the state graph and add nodes."""
    # Initialize the state graph with the state class
    def __init__(self,tool_node):
        self.tool_node=tool_node
        self.toolcall=ToolCall(self.tool_node)
        self.call=self.toolcall.call 
    def graph_run(self):    
        model=StateGraph(State)
        tool_node=ToolNode([self.tool_node])
        model.add_node("retriever_tool",tool_node)
        model.add_node('Agent',self.call)
        model.add_node('generate',generator)
        model.add_node('rewrite',rewrite)

        model.add_edge(START,'Agent')
        model.add_conditional_edges(
        "Agent",
        # Assess agent decision
        tools_condition,
        {
            # Translate the condition outputs to nodes in our graph
            "tools": "retriever_tool",
            "__end__": END,
        },
        )
        model.add_conditional_edges("retriever_tool",grader,{'rewrite':'rewrite','generate':'generate'})
        #model.add_edge('retriever_tool',END)
        model.add_edge("generate",END)
        model.add_edge('rewrite','Agent')
        graph=model.compile()
     
        return graph


