def get_bot_response(user_input):
    user_input = user_input.lower()

    responses = {
        "hello": "Hi there! How can I assist you?",
        "hi": "Hello! How may I help you today?",
        "how are you": "I'm just a bot, but I'm functioning well!",
        "what is your name": "I am a smart chatbot developed using Flask.",
        "bye": "Goodbye! Have a nice day!",
    }

    return responses.get(user_input, "Sorry, I don't understand that. Can you rephrase?")
