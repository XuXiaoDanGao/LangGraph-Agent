from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict
from langchain_core.messages import HumanMessage

class State(TypedDict):
    messages: list

def node(state: State):
    return {"messages": state["messages"] + [HumanMessage(content="Test from LangGraph 1.0 OK!")]}

graph = StateGraph(State)
graph.add_node("test", node)
graph.add_edge(START, "test")
graph.add_edge("test", END)

app = graph.compile()
result = app.invoke({"messages": [HumanMessage(content="hi")]})
print(result)