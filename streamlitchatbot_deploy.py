import os
import streamlit as st
import textwrap
from IPython.display import display
from IPython.display import Markdown
import google.generativeai as genai



genai.configure(api_key="AIzaSyDzfxB1MfwjpnEtm1QKUwl-WnfgOosV3go")
model=genai.GenerativeModel('gemini-pro')


if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history = [])

st.title("ILineCare")
#st.write("Welcome, I am Medibot 🤖")

with st.chat_message("assistant"):
        st.markdown("Welcome, I am Medibot 🤖")
        st.markdown("Ask me a question by providing your symptoms and I will try to predict the dieases and help you with the best possible solution.")


#st.write("Ask me a question by providing your symptoms and I will try to predict the dieases and help you with the best possible solution.")



def role_to_streamlit(role):
     if role=="model":
          return "assistant"
     else:
          return role


for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)

try:
    

    if prompt := st.chat_input("What can I do for you?"):
        st.chat_message("user").markdown(prompt)
        if "itching" in prompt or "skin rash" in prompt:
            response = "You may have Fungal Infection"
            with st.chat_message("assistant"):
                st.markdown(response)
        else:
            response=st.session_state.chat.send_message(prompt)
            with st.chat_message("assistant"):
                st.markdown(response.text)
except Exception as e:
    print(e)
    response="I couldn't understood , Please try by updating your prompt"
    with st.chat_message("assistant"):
            st.markdown(response)
