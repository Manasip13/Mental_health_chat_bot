import os
from huggingface_hub import InferenceClient  # Import the Hugging Face inference client
from dotenv import load_dotenv  # Import dotenv to load API keys securely

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("HF_API_KEY")  # Retrieve the API key from the environment variables

# Initialize Hugging Face Inference Client using the API key
client = InferenceClient(api_key=API_KEY)

def get_response(user_input):
    """
    Fetches response from the Hugging Face model.
    
    Args:
        user_input (str): The input text from the user.

    Returns:
        str: The generated response from the model or an error message.
    """
    try:
        # Define the chat message format as required by the model
        messages = [{"role": "user", "content": user_input}]

        # Call the Hugging Face model for text completion
        completion = client.chat.completions.create(
            model="google/gemma-2-2b-it",  # Specify the model to use
            messages=messages,  # Pass user messages
            max_tokens=500  # Limit response length
        )

        # Extract and return the generated response from the model
        return completion.choices[0].message["content"]
    
    except Exception as e:
        # Handle any errors and return the error message
        return f"Error: {str(e)}"
