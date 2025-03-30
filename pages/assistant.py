import os
from openai import OpenAI
import streamlit as st
import shutil

if os.getenv("RENDER"):
    secrets_src = "/etc/secrets/secrets.toml"
    secrets_dest = os.path.expanduser("~/.streamlit/secrets.toml")

    os.makedirs(os.path.dirname(secrets_dest), exist_ok=True)
    shutil.copy(secrets_src, secrets_dest)

openai_api_key = st.secrets["openai"]["api_key"]
client = OpenAI(api_key=openai_api_key)

knowledge = st.secrets.get("knowledge", {}).get("knowledge_base", "")

st.title("Wally 🤖 Personal Chatbot")

with st.expander("ℹ️ Disclaimer"):
    st.write(
        """
        This chatbot is designed to assist with questions about Kevin Van Wallendael.
        While it strives to provide accurate and helpful information, all responses should
        be independently verified if used for decision-making purposes.

        The assistant’s knowledge is derived from the information provided at runtime.
        Responses may vary based on input phrasing or context.
        """
    )

if "messages" not in st.session_state:
    if knowledge:
        system_message = f"""
        You are a helpful assistant. Your core functionality is to answer questions about Kevin Van Wallendael.
        You are his personal coding portfolio assistant for external people to interact with.
        Here is some information about him:
        {knowledge}
        When responding to user questions, please summarize or extract only the relevant information from the provided knowledge. Limit your response length when talking specifically about him. 
        We want to encourage follow up questions and a flowing conversation. Feel free to use emojis to make you appear friendly and cool. Kevin is Gen-Z and loves the cool emojis.
        """
    else:
        system_message = "You are a helpful assistant. Your core functionality is to answer questions about Kevin Van Wallendael. You are his portfolio assistant for external people to interact with."

    st.session_state.messages = [{"role": "system", "content": system_message}]

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything!"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages,
            max_tokens=300,
            temperature=0.7,
        )

        assistant_reply = response.choices[0].message.content.strip()

        with st.chat_message("assistant"):
            st.markdown(assistant_reply)

        st.session_state.messages.append({"role": "assistant", "content": assistant_reply})

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")