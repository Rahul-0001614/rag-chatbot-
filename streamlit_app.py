
import streamlit as st
from rag import ask_question

st.title("PDF RAG Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Clear button
if st.button("🗑️ New Chat"):
    st.session_state.messages = []
    st.rerun()

# Chat input
question = st.chat_input("Ask a question")

if question:
    st.session_state.messages.append({"role": "user", "content": question})

    answer = ask_question(question)

    st.session_state.messages.append({"role": "assistant", "content": answer})

# Display chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])