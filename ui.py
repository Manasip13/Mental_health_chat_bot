import streamlit as st  # Import Streamlit for building the web app
from model_load import get_response  # Import the function to fetch AI responses

# ===========================
# Page Configuration
# ===========================
st.set_page_config(
    page_title="Mental Health AI Chatbot",  # Title of the page
    page_icon="🤖",  # Page icon
    layout="centered"  # Center the page layout
)

# ===========================
# Custom CSS for Styling
# ===========================
st.markdown("""
    <style>
        /* Set background color and image */
        body {
            background-color: #141414;
            background-image: url("https://images.unsplash.com/photo-1521747116042-5a810fda9664");
            background-size: cover;
            background-position: center;
            margin: 0;
            padding: 0;
            height: 100vh;
        }

        /* Main container styling */
        .main {
            background: transparent;
            color: black;
        }

        /* Chat container for centering messages */
        .chat-container {
            max-width: 600px;
            margin: auto;
            padding: 20px;
        }

        /* User message styling */
        .user-message {
            text-align: right;
            background-color: #89d9f2;
            padding: 12px;
            border-radius: 20px;
            max-width: 70%;
            margin-left: auto;
            color: black;
        }

        /* AI bot message styling */
        .bot-message {
            text-align: left;
            background-color: #232323;
            padding: 12px;
            border-radius: 20px;
            max-width: 70%;
            color: white;
        }

        /* Message container for alignment */
        .message-container {
            display: flex;
            align-items: center;
            margin-bottom: 10px;
        }

        /* Avatar image styling for bot */
        .avatar {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            margin-right: 10px;
        }

        /* Chatbot header styling */
        .header {
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# ===========================
# Chatbot UI Header
# ===========================
st.markdown('<div class="header">🧠 Mental Health AI Bot</div>', unsafe_allow_html=True)

# ===========================
# Initialize Chat History
# ===========================
if "messages" not in st.session_state:
    # Start with a welcome message from the AI assistant
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! 😊 I'm your AI assistant. How can I help you today?"}
    ]

# ===========================
# Display Chat History
# ===========================
for msg in st.session_state.messages:
    if msg["role"] == "user":
        # Display user messages on the right side
        st.markdown(f'<div class="message-container"><div class="user-message">{msg["content"]}</div></div>', unsafe_allow_html=True)
    else:
        # Display AI bot messages on the left side with an avatar
        st.markdown(f'''
            <div class="message-container">
                <img src="https://cdn-icons-png.flaticon.com/512/4712/4712031.png" class="avatar">
                <div class="bot-message">{msg["content"]}</div>
            </div>
        ''', unsafe_allow_html=True)

# ===========================
# User Input Section
# ===========================
user_input = st.chat_input("Type your message...")  # Get user input

if user_input:
    # Append user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.markdown(f'<div class="message-container"><div class="user-message">{user_input}</div></div>', unsafe_allow_html=True)

    # ===========================
    # Get AI Response
    # ===========================
    with st.chat_message("assistant"):  # Display AI response in chat
        try:
            response = get_response(user_input)  # Fetch response from AI model
        except Exception as e:
            response = "⚠️ I'm having trouble responding. Please try again later."  # Handle errors

    # Append AI response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.markdown(f'''
        <div class="message-container">
            <img src="https://cdn-icons-png.flaticon.com/512/4712/4712031.png" class="avatar">
            <div class="bot-message">{response}</div>
        </div>
    ''', unsafe_allow_html=True)
