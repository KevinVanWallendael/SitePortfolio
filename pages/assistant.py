import os
from openai import OpenAI
import streamlit as st
import shutil
import toml 

if os.getenv("RENDER"):
    secrets_src = "/etc/secrets/secrets.toml"
    secrets_dest = os.path.expanduser("~/.streamlit/secrets.toml")

    os.makedirs(os.path.dirname(secrets_dest), exist_ok=True)
    shutil.copy(secrets_src, secrets_dest)

openai_api_key = st.secrets["openai"]["api_key"]
client = OpenAI(api_key=openai_api_key)

# Streamlit app UI
st.title("Wally - Personal Chatbot")

with st.expander("ℹ️ Disclaimer"):
    st.write(
        """
        This chatbot is designed to assist with questions about Kevin Van Wallendael.
        While it strives to provide accurate and helpful information, all responses should
        be independently verified if used for decision-making purposes.
        
        The assistant’s knowledge is derived from the information provided at runtime, 
        including documents fetched from S3. Responses may vary based on input phrasing or context.
        """
    )

# Initialize the messages in session state if not already done
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant. Your core functionality is to answer questions about Kevin Van Wallendael." 
        "You are his portfolio assistant for external people to interact with."}
    ]

# Display previous messages (exclude system message)
for message in st.session_state.messages:
    if message["role"] != "system":  # Skip displaying the system message
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Capture new prompt and handle response
if prompt := st.chat_input("Ask me anything!"):
    # Append user's message to the session state
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Show the user's message in the chat
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # Send the updated messages to OpenAI API for response
        response = client.chat.completions.create(
            model="gpt-4o-mini",  
            messages=st.session_state.messages,  
            max_tokens=150,
            temperature=0.7,
        )

        # Get the assistant's response
        assistant_reply = response.choices[0].message.content.strip()

        # Show the assistant's reply in the chat
        with st.chat_message("assistant"):
            st.markdown(assistant_reply)

        # Append assistant's response to session state
        st.session_state.messages.append({"role": "assistant", "content": assistant_reply})

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
