def simple_chatbot():
    print("Basic Chatbot: Hello! Type something to talk to me. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input == 'bye':
            print("Chatbot: Goodbye! Have a nice day!")
            break
        elif 'hello' in user_input or 'hi' in user_input:
            print("Chatbot: Hi there!")
        elif 'how are you' in user_input:
            print("Chatbot: I'm fine, thanks! How about you?")
        elif 'your name' in user_input:
            print("Chatbot: I'm just a simple chatbot.")
        elif 'thank' in user_input:
            print("Chatbot: You're welcome!")
        else:
            print("Chatbot: I didn't understand that. Can you try something else?")

# Start the chatbot
if __name__ == "__main__":
    simple_chatbot()
