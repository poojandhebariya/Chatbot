import streamlit as st
import pandas as pd
import pyperclip
from chat_module import predict_disease_from_symptom

# Load the dataset into a pandas dataframe
df = pd.read_excel(r'dataset.xlsx')

# Get all unique symptoms
symptoms = set()
for s in df['Symptoms']:
    for symptom in s.split(','):
        symptoms.add(symptom.strip())

# Add a sidebar for symptoms selection
st.sidebar.title("Select Symptoms")
selected_symptoms = st.sidebar.multiselect("Choose Symptoms", list(symptoms))

# Add a button to copy selected symptom to clipboard
if st.sidebar.button("Copy Selected Symptom"):
    if selected_symptoms:
        # Concatenate selected symptoms into a single string
        selected_symptom_text = ", ".join(selected_symptoms)
        pyperclip.copy(selected_symptom_text)
        # Copy selected symptoms to clipboard
        #st.sidebar.text_area("Copy Selected Symptom", selected_symptom_text, height=30)
        st.sidebar.text("Symptom copied to clipboard!")
    else:
        st.sidebar.warning("Please select at least one symptom!")



def role_to_streamlit(role):
    if role=="model":
        return "assistant"
    else:
        return role


if 'chat' not in st.session_state:
    st.session_state.chat = {
        'history': []
    }

with st.chat_message("assistant"):
    st.write(" Hello there! Welcome to Medibot, your personal health assistant. Ready to decode those symptoms and uncover the mystery behind your health concerns? Let's embark on a journey to pinpoint the issue and guide you towards the path of wellness.How can I assist you today?")


with st.container():
    for message in st.session_state.chat['history']:  # Accessing 'history' directly from st.session_state.chat
        with st.chat_message(role_to_streamlit(message['role'])):
            st.markdown(message['content'])





prompt = st.chat_input("What can I do for you?")
if prompt:
    flag = 1
    prompt_elements = prompt.split(",")
    for i in prompt_elements:
        if i.strip() not in symptoms:  # Use strip() to remove leading/trailing spaces
            flag = 0
            break  # Exit the loop early if any symptom is not in the list

    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.chat['history'].append({"role": "User", "content": prompt})

    if flag == 1:
        # Call predict_disease_from_symptom function from chat_module.py
        predicted_disease = predict_disease_from_symptom(prompt_elements)  # Use prompt_elements here
        with st.chat_message("assistant"):
            output = "You may have " + predicted_disease
            st.markdown(output)
    else:
        
        with st.chat_message("assistant"):
            output = "Please provide symptoms from the list given in the sidebar"
            st.markdown(output)

    st.session_state.chat['history'].append({"role": "assistant", "content": output})
