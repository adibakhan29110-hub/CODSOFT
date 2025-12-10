def get_bot_response(message):

    msg = message.lower()

    # Basic greetings
    if "hello" in msg or "hi" in msg:
        return "Hello! How can I help you today? 😊"

    # Asking name
    elif "your name" in msg:
        return "I'm Nova, your rule-based chatbot assistant! ✨"

    # Asking about chatbot
    elif "what can you do" in msg:
        return "I can answer your questions, chat with you, and help you with basic tasks!"

    # Feelings
    elif "how are you" in msg:
        return "I'm doing great! Thanks for asking ❤️"

    # Goodbye
    elif "bye" in msg:
        return "Goodbye! Have a great day! 🌸"

    # More advanced patterns
    elif "weather" in msg:
        return "I cannot fetch live weather yet, but you can check using a weather app! ⛅"

    elif "joke" in msg:
        return "Why don't robots panic? Because we have nerves of steel! 😄"

    elif "love" in msg:
        return "Love is a beautiful feeling. Be kind to yourself ❤️"

    # Default fallback
    else:
        return "I'm not sure I understand that, but I'm learning every day! 🤖✨"
