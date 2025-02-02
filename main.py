'''
#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
import os
#import dotenv
from dotenv import load_dotenv

load_dotenv()

#print(os.getenv("API_KEY"))

groq_api_key=os.getenv("groq_api_key")

#print(groq_api_key)
from typing import TypedDict, Annotated

from pydantic import BaseModel
from langgraph.graph import StateGraph, add_messages, START , END
class State(TypedDict):
    messages:Annotated[list, add_messages]

from langchain_groq import ChatGroq

llm = ChatGroq(groq_api_key=groq_api_key, model_name="Gemma2-9b-It")

#print(llm.invoke(["Hello"]))

def chatbot(state: State):
    return{"messages": llm.invoke(state["messages"])}

#creating chatbot graph using stategraph(which we imported from langgraph)
graph=StateGraph(State)
graph.add_node("chatbot",chatbot)
graph.add_edge(START,"chatbot")

my_chatbot=graph.compile()

##bring chatbot into the life

while True:#this loop run untill you type exit
    user_input=input("You: ")
    if user_input=="exit":
        print("Chatbot: GoodBye!")
        break
    for event in graph.stream({"messages":("user", user_input)}):
        print(event.values())
        for value in event.values():
            print("Assistant: ",value["messages"].content)
           '''
'''
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the Groq API key from the environment
groq_api_key = os.getenv("groq_api_key")

# Import required modules
from typing import TypedDict, Annotated
from pydantic import BaseModel
from langgraph.graph import StateGraph, add_messages, START, END
from langchain_groq import ChatGroq

# Define the state dictionary to handle messages
class State(TypedDict):
    messages: Annotated[list, add_messages]

# Initialize the ChatGroq model
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Gemma2-9b-It")

# Define the chatbot function to invoke the Groq API
def chatbot(state: State):
    return {"messages": llm.invoke(state["messages"])}

# Create the StateGraph and add the chatbot as a node
graph = StateGraph(State)
graph.add_node("chatbot", chatbot)
graph.add_edge(START, "chatbot")

# Compile the graph
my_chatbot = graph.compile()

# Bring the chatbot to life with a loop for user input
while True:  # this loop runs until you type "exit"
    user_input = input("You: ")
    if user_input == "exit":
        print("Chatbot: Goodbye!")
        break
    
    # Directly call the chatbot function
    state = {"messages": [("user", user_input)]}
    response = chatbot(state)  # calling the chatbot function directly
    
    # Print the response content
    print("Assistant: ", response["messages"].content)
'''
import os
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the Groq API key from the environment
groq_api_key = os.getenv("groq_api_key")

# Import required modules
from typing import TypedDict, Annotated
from pydantic import BaseModel
from langgraph.graph import StateGraph, add_messages, START, END
from langchain_groq import ChatGroq

# Define the state dictionary to handle messages
class State(TypedDict):
    messages: Annotated[list, add_messages]

# Initialize the ChatGroq model
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Gemma2-9b-It")

# Define the chatbot function to invoke the Groq API
def chatbot(state: State):
    return {"messages": llm.invoke(state["messages"])}

# Create the StateGraph and add the chatbot as a node
graph = StateGraph(State)
graph.add_node("chatbot", chatbot)
graph.add_edge(START, "chatbot")

# Compile the graph
my_chatbot = graph.compile()

# Streamlit interface setup
st.title("Chatbot  :) Ask me Anything I will Assist You ;)")

# Input and output handling
user_input = st.text_input("You:", "")
if user_input:  # If the user enters input
    state = {"messages": [("user", user_input)]}
    response = chatbot(state)  # calling the chatbot function directly
    
    # Display the response content from the assistant
    st.write("Assistant: ", response["messages"].content)

# Optionally, a stop button
if st.button('Exit'):
    st.write("Chatbot: Goodbye!")

