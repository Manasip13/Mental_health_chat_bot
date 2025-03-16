import streamlit as st  # Ensure this line is at the top of your script
from huggingface_hub import InferenceClient

# Access the Hugging Face API key from Streamlit secrets
API_KEY = st.secrets["HF_API_KEY"]

# Initialize Hugging Face Inference Client
client = InferenceClient(api_key=API_KEY)

def get_response(user_input):
    """Fetches response from the Hugging Face model."""
    try:
        messages = [{"role": "user", "content": user_input}]

        completion = client.chat.completions.create(
            model="google/gemma-2-2b-it",
            messages=messages,
            max_tokens=500
        )

        return completion.choices[0].message["content"]
    
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("Hugging Face Model with Streamlit")

input_text = st.text_area("Enter your input:", "Hello, how can I help you today?")
if st.button("Generate Response"):
    if input_text:
        response = get_response(input_text)
        st.write(response)
    else:
        st.write("Please enter some text.")
