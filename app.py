import streamlit as st
import requests

# 1. Page Configuration
st.set_page_config(page_title="Personal Assistant", layout="centered")

# 2. Custom CSS for UI
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: white; }
    input::placeholder { color: #888888 !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. UI Header
st.header("🤝 Your Personal Assistant")
st.write("1. Answer questions on various topics.")
st.write("2. Arrange Calendar events and meetings.")
st.write("3. Read emails, send replies, and summarize.")
st.write("4. Manage tasks and to-do lists.")
st.write("5. Take quick notes.")
st.write("6. Track expenses.")

st.markdown("### 💬 Chat with your assistant")

# 4. Chat Input & n8n Trigger
if prompt := st.chat_input("H"):
    # Display user message locally
    with st.chat_message("user"):
        st.markdown(prompt)

    # Trigger n8n Webhook
    try:
        payload = {"chat_input": prompt}
        # Using the specific URL you provided earlier
        n8n_url = "https://soham95.app.n8n.cloud/webhook-test/10e1efd3-8b5a-4f18-8c27-a6e54d6a14ca"
        
        response = requests.post(n8n_url, json=payload)
        
        if response.status_code == 200:
            st.toast("Sent to n8n!")
        else:
            st.error(f"Error {response.status_code}: Check if n8n is 'Listening'")
            
    except Exception as e:
        st.error(f"Failed to connect: {e}")
