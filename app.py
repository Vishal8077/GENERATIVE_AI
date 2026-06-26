import streamlit as st
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

st.set_page_config(page_title="Vishal AI Agent", page_icon="🤖")
st.title("🤖 Vishal AI Agent")

@st.cache_resource
def get_model():
    llm_endpoint = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-R1")
    return ChatHuggingFace(llm=llm_endpoint)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    model = get_model()
    with st.spinner("Thinking..."):
        response = model.invoke(prompt)

    st.session_state.messages.append({"role": "assistant", "content": response.content})
    st.chat_message("assistant").write(response.content)
