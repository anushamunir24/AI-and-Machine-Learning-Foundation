responses = {
    "hello" : "Hello! How can I help you today?",
    "hi" : "Hi there! What can I do for you?",
    "hye" : "Hye! How are you doing?",
    "how are you" : "I'm doing great. How about you?",
    "i'm fine" : "That's good to hear! Is there anything specific you'd like to talk about or ask?",
    "what is your name" : "I am a chat bot. What is your name?",
    "what is the weather like" : "I'm sorry, I don't have access to real-time weather information. You can check a weather website or app for the latest updates.",
    "what is chatbot" : "A chatbot is a computer program designed to simulate conversation with human users, especially over the Internet. I am an example of a chatbot.",
    "what is ai" : "AI stands for Artificial Intelligence. It refers to the simulation of human intelligence in machines that are programmed to think and learn like humans.",
    "what can you do" : "I can assist you with various tasks, answer your questions, and provide information. Just ask me.!",
    "i'm learning artificial intelligence" : "That's fantastic! AI is an exciting field with a lot of potential.",
    "i got my first project" : "Congratulations! What is your project about?",
    "i'm working on a chatbot project" : "That sounds interesting! Chatbots are a great way to learn about AI and natural language processing. Good luck with your project!",
    "bye" : "Goodbye!"
}

print("Bot: Hello! I am a chatbot. You can ask me anything or type 'exit' to end the conversation.")

while True:
    raw_input = input("You: ")
    clean_input = raw_input.lower().strip()
    if clean_input == "exit":
        print("Bot: GoodBye! Have a great day!")
        break 
    reply = responses.get(clean_input, "I don't understand, can you please say again?")
    print("Bot: " + reply)