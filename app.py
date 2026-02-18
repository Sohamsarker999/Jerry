import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Personal Assistant", layout="centered")

# 2. Custom CSS for the "Pitch Black" UI & Bottom Input
st.markdown("""
    <style>
    /* Background of the main app */
    .stApp {
        background-color: #000000;
        color: white;
    }
    /* Style the Chat Input at the bottom */
    .stChatInputContainer {
        padding-bottom: 20px;
    }
    /* Placeholder text color */
    input::placeholder {
        color: #888888 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. UI Header
st.header("🤝 Your Personal Assistant")
st.subheader("What can your personal assistant do?")

# 4. Feature List
features = [
    "1. Answer questions on various topics.",
    "2. Arrange Calendar events and meetings.",
    "3. Read your emails and send replies, can even summarize them for you.",
    "4. Manage your tasks and to-do lists.",
    "5. Take quick notes for you.",
    "6. Track your expenses and budgeting."
]

for feature in features:
    st.write(feature)

st.markdown("### 💬 Chat with your assistant")

# 5. Chat History Placeholder (Needed for logic)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 6. Chat Input at the bottom
if prompt := st.chat_input("H"):
    # Here you can add logic to trigger n8n or an LLM
    with st.chat_message("user"):
        st.markdown(prompt)
