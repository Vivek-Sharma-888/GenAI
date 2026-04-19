from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st
load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

st.title("My QnA Bot")
st.markdown("A chat bot using Langchain and OpenAi")

if not st.session_state:
    st.session_state.messages =[]

for message in st.session_state.messages:
    role = message["role"]
    content=message["content"]
    st.chat_message(role).markdown(content)

query= st.chat_input("Ask anything")
if query:
    st.session_state.messages.append({"role":"user","content":query})
    st.chat_message("user").markdown(query)
    res= llm.invoke(query)
    st.session_state.messages.append({"role":"ai","content":res.content})
    st.chat_message("ai").markdown(res.content)

