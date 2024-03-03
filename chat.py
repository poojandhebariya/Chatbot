import streamlit as st


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
    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.chat['history'].append({"role": "User", "content": prompt})

    if "itching" in prompt.lower() or "skin rash" in prompt.lower():
            output = "You may have Fungal Infection"
            with st.chat_message("assistant"):
                st.markdown(output)
    elif "visual disturbances" in prompt.lower() or "irritability" in prompt.lower() or "depression" in prompt.lower():
            output = "You may have Migraine"
            with st.chat_message("assistant"):
                st.markdown(output)
    elif "migraine" in prompt.lower():
         output="Migraine is a neurological disorder characterized by recurrent episodes of severe headaches, often accompanied by other symptoms such as nausea, vomiting, and sensitivity to light and sound. These episodes, known as migraine attacks, can be debilitating and significantly impact a person's quality of life.Here are some key points to include when discussing migraine disease:\n\n**Symptoms:** Migraine headaches typically present as a pulsating or throbbing pain, usually on one side of the head. The pain can be moderate to severe and may last for hours to days. Other common symptoms include nausea, vomiting, and sensitivity to light, sound, and certain smells.\n\n**Types:** Migraine can be classified into several types, with the most common being migraine without aura and migraine with aura. Aura refers to sensory disturbances that often precede or accompany the headache, such as visual disturbances (flashes of light, blind spots), sensory changes, or speech disturbances.\n\n**Triggers:** Migraine attacks can be triggered by various factors, including hormonal changes (such as menstruation), certain foods and drinks (such as aged cheeses, alcohol, and caffeine), stress, lack of sleep, sensory stimuli (such as bright lights or strong smells), and environmental factors.\n\n**Pathophysiology:** The exact cause of migraine is not fully understood, but it is believed to involve a complex interplay of genetic, environmental, and neurological factors. Dysfunction in the brainstem and abnormal activity in certain brain chemicals, such as serotonin, are thought to play a role in migraine pathophysiology.\n\n**Treatment:** Treatment for migraines aims to relieve symptoms and prevent future attacks. This may include over-the-counter or prescription medications for acute pain relief (such as nonsteroidal anti-inflammatory drugs or triptans), preventive medications to reduce the frequency and severity of attacks, lifestyle modifications (such as stress management techniques and regular sleep schedules), and alternative therapies (such as acupuncture or biofeedback).\n\n**Impact on Daily Life::** Migraine can have a significant impact on various aspects of daily life, including work, school, relationships, and social activities. Chronic migraines, which involve frequent or daily headache episodes, can be particularly disabling and may require more intensive treatment approaches.\n\n**Seeking Medical Advice:** It's important for individuals experiencing migraines to seek medical advice for proper diagnosis and management. A healthcare provider can help develop an individualized treatment plan tailored to the person's specific needs and preferences."
         with st.chat_message("assistant"):
                st.markdown(output)
    else:
        output = "Please provide  more specific information."
        with st.chat_message("assistant"):
            st.markdown(output)
    st.session_state.chat['history'].append({"role": "assistant", "content": output})