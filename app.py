import getpass
import os

os.environ["SLACK_USER_TOKEN"] = ""
from langchain_openai import ChatOpenAI

#llm = ChatOpenAI(model="gpt-4o-mini")

import streamlit as st
from langchain_openai.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.tools.retriever import create_retriever_tool
from langchain.agents import AgentExecutor, Tool, AgentType, create_json_chat_agent
from langchain.agents.react.agent import create_react_agent
from langchain import hub

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import ConfigurableField
from langchain_core.tools import tool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_community.agent_toolkits import SlackToolkit

st.title("🦜🔗 App")

openai_api_key = st.sidebar.text_input("OpenAI API Key")
#slack_user_token = st.sidebar.text_input("Slack user token")

file = st.file_uploader("Upload a PDF file", type="pdf")
tmp_location = os.path.join(file.name)
def generate_response(input_text):
    loader = PyPDFLoader(tmp_location)
    pages = loader.load()

    text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=150,
    length_function=len)
    docs = text_splitter.split_documents(pages)
    embedding = OpenAIEmbeddings(api_key=openai_api_key)
    vectordb = Chroma.from_documents(documents=docs,embedding=embedding)

    toolkit = SlackToolkit()
    tool = toolkit.get_tools()
    tool1 = tool[3].as_tool(name = 'slack', description='send message on slack')
    tool2 = create_retriever_tool(retriever=vectordb.as_retriever(), name = 'Retrival_tool', description='Retrival_tool_for_documentdb')
    tools = [tool2, tool1]

    llm = ChatOpenAI(model="gpt-4o-mini",api_key=openai_api_key)
    prompt = ChatPromptTemplate.from_messages([
    ("system", "you're a helpful assistant"), 
    ("human", "{input}"), 
    ("placeholder", "{agent_scratchpad}"),])
    agent = create_tool_calling_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    st.info(agent_executor.invoke({"input":input_text}))


with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What is the company name?",
    )
    submitted = st.form_submit_button("Submit")
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")
    if submitted and openai_api_key.startswith("sk-"):
        generate_response(text)