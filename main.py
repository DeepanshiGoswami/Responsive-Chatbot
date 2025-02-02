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

