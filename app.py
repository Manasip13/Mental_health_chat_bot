# Import the get_response function from model_load module
from model_load import get_response

def chatbot():
    """
    A simple chatbot that interacts with the user through the command line.
    The chatbot uses the Hugging Face model to generate responses.

    The user can type messages, and the chatbot will respond.
    Typing 'exit' will terminate the conversation.
    """
    print("Welcome to the Hugging Face Chatbot! Type 'exit' to quit.")  # Greeting message

    while True:  # Infinite loop to keep the chatbot running
        user_input = input("You: ")  # Take input from the user

        # Check if the user wants to exit the chatbot
        if user_input.lower() == "exit":
            print("Goodbye!")  # Print exit message
            break  # Exit the loop and end the program

        # Get AI-generated response from the model
        response = get_response(user_input)

        # Display the AI's response
        print(f"AI: {response}")

# Ensure the chatbot runs only when the script is executed directly
if __name__ == "__main__":
    chatbot()  # Start the chatbot
