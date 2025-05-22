from src.graphstate import State
from langchain_core.messages import HumanMessage
from src.llmUtils.llm import get_llm


def rewrite(state:State):
    """
    Transform the query to produce a better question.

    Args:
        state (messages): The current state

    Returns:
        dict: The updated state with re-phrased question
    """

    print("---TRANSFORM QUERY---")
    
    question = state['query'].content

    msg = [
        HumanMessage(
            content=f""" \n 
    Look at the input and try to reason about the underlying semantic intent / meaning. \n 
    Here is the initial question:
    \n ------- \n
    {question} 
    \n ------- \n
    Formulate an improved question: """,
        )
    ]
    llm=get_llm()
    # Grader
    
    response = llm.invoke(msg)
    return {"query": [response]}