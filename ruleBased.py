def chatbot():
    while True:
        user_input = input("You: ").lower()
        if "hello" in user_input:
            print("Bot: Hi there!")
        elif "bye" in user_input:
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: I'm not sure how to respond.")

chatbot()
