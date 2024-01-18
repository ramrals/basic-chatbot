# Importing the necessary libraries
import random

# Defining the chatbot function
def chatbot():
    # List of possible responses
    responses = [
        "Hello!",
        "How can I assist you today?",
        "I'm here to help!",
        "What can I do for you?",
        "Feel free to ask me anything."
    ]

    # Chatbot loop
    while True:
        # Getting user input
        user_input = input("> ")

        # Checking for exit command
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Generating a random response
        random_response = random.choice(responses)
        print(random_response)

# Running the chatbot function
chatbot()
