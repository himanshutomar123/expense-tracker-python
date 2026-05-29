#                                     --------------------------------------- PERSONAL CHAT ASSISTANT ---------------------------------------

# OBJECTIVE = CREATE A CONVERSATIONAL AI ASSISTANT USING PYTHON CORE LOGIC

print("Welcome to rule based chat box.")
print("Hello! I'm Himanshu.")
print("You can ask me basic questions. Type 'bye' to exit from the bot.")

# Chatbot Memory Creation [Dictionary of responses]
response = {
    "hello": "Hi Welcome, how can I help you?",
    "how are you": "I am very fine. Thank You.",
    "who are you": "I am a smart AI chatbot.",
    "motivate me": "Keep Going Until You get success.",
    "happy": "Great to hear that."
}


def get_response(user_q):
    user_q = user_q.lower()

    for key in response:
        if key in user_q:
            return response[key]

    return "I DON'T KNOW"


# Chat Loop
while True:
    user_input = input("\nAsk Questions: ")

    if "bye" in user_input.lower():
        print("Bot: Goodbye! Have a nice day.")
        break

    reply = get_response(user_input)
    print("Bot:", reply)