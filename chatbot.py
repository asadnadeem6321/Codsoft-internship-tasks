def simple_chatbot(user_input):
    # Define some rules and responses
    responses = {
        "hi": "Hello! How can I assist you?",
        "how are you?": "I'm just a bot, but I'm functioning perfectly!",
        "bye": "Goodbye! Have a great day!",
        "what is your name?": "I'm just a simple chatbot.",
        "tell me about computer?" : "Computer is an electronic machine used for solving mathematical expressions and real world problems.",
        "tell me about ai?" : "Artificial Intelligence is about principle of can machine think, When this question is spreading, The Artificial Intelligence is born ",
        "Tell me about CS?" : "Computer science focuses on the development and testing of software and software systems.",
        "Tell me about IT?" : "nformation technology (IT) is the use of any computers, storage, networking and other physical devices, infrastructure and processes to create, process, store, secure and exchange all forms of electronic data.",
        "how AI is helping to improve education?" : "AI in schools helps students by offering personalized learning experiences. By analyzing data on each student's strengths and weaknesses, AI can create customized learning plans that cater to each student's needs. ",
        "tell me about computer vision?" : "Computer vision is a field of artificial intelligence (AI) that uses machine learning and neural networks to teach computers and systems to derive meaningful information from digital images, videos and other visual inputs—and to make recommendations or take actions when they see defects or issues.",
        "tell me about nlp?": "Natural Language Processing (NLP) allows machines to break down and interpret human language. It's at the core of tools we use every day – from translation software, chatbots, spam filters, and search engines, to grammar correction software, voice assistants, and social media monitoring tools.",
        "default": "I'm sorry, I don't understand. Can you please rephrase?"
    }

    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Check if the user input matches any rule, otherwise use the default response
    response = responses.get(user_input, responses["default"])
    
    return response

# Main loop for chatting
def chat():
    print("Welcome to the simple chatbot!")
    print("Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(simple_chatbot(user_input))
            break
        else:
            print("Bot:", simple_chatbot(user_input))

# Start the chat
chat()
