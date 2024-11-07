from flask import Flask, Blueprint, request, jsonify
import datetime

chatbot = Blueprint('chatbot', __name__)

events=[
  {
    "title": "EventZen",
    "date": "12 Jan 2023 - 15 Jan 2023",
    "details": "Our inaugural EventZen with 450+ participants and 1000+ registrations in various competitions. A huge success!"
  },
  {
    "title": "Aavhan",
    "date": "24 April 2023 - 26 April 2023",
    "details": "Aavhan’s second edition featured a wide range of curricular and extra-curricular competitions, celebrating talent and success!"
  },
  {
    "title": "EventZen2.0",
    "date": "08 March 2024 - 11 March 2024",
    "details": "EventZen 2.0: A blend of coding, gaming, AI design, and BGMI battles. Connect, learn, and compete!"
  },
  {
    "title": "EventZen 3.0",
    "date": "26 Oct 2024 - 27 Oct 2024",
    "details": "EventZen 3.0: A creative gaming and learning experience with coding, quizzes, film, AI, and BGMI battles!"
  }
]
upcomingEvents=[
    {
    "title": "EventZen 4.0",
    "date": "26 April 2025 - 27 April 2025",
    "details": "EventZen 4.0: A creative gaming and learning experience with coding, quizzes, film, AI, and BGMI battles!"
  }
]

faq = {
    "Hello": "Hello! How can I help you?",
    "Hii": "Hii! How can I help you?",
    "What is Team Ignite?": "Team Ignite is a student association focused on organizing events and workshops to enhance personal and professional growth.",
    "How can I join Team Ignite?": "To become a member, visit the 'Contact' section of our website and contact us.",
    "How can I register for events?": "You can register for events directly through our website by filling out the event registration form from event tab."
}

# Define the /chatbot endpoint to handle POST requests
@chatbot.route('/', methods=['POST'])
def chatbot_response():
    user_message = request.json.get("message")
    response = {"reply": "I'm sorry, I couldn't understand that. Can you ask me something else?"}

    if "event" in user_message.lower():
        response["reply"] = "Here are our past events:\n"
        for event in events:
            response["reply"] += f"\n{event['title']} - {event['date']}\n{event['details']}\n"
    if "upcoming event" in user_message.lower():
        response["reply"] = "Here are our upcoming events:\n"
        for upevent in upcomingEvents:
            response["reply"] += f"\n{upevent['title']} - {upevent['date']}\n{upevent['details']}\n"

    elif "team ignite" in user_message.lower():
        response["reply"] = faq.get("What is Team Ignite?", response["reply"])
    elif "hello" in user_message.lower():
        response["reply"] = faq.get("Hello", response["reply"])
    elif "hi" in user_message.lower():
        response["reply"] = faq.get("Hii", response["reply"])
    elif "join" in user_message.lower() or "membership" in user_message.lower():
        response["reply"] = faq.get("How can I join Team Ignite?", response["reply"])
    elif "register" in user_message.lower() or "sign up" in user_message.lower():
        response["reply"] = faq.get("How can I register for events?", response["reply"])

    return jsonify(response)

#####################################

#basic code
# from flask import Blueprint, request, jsonify

# # Define the chatbot blueprint
# chatbot = Blueprint('chatbot', __name__)

# # Simple chatbot logic to process the message
# @chatbot.route('/', methods=['POST'])
# def chatbot_response():
#     user_message = request.json.get("message")
#     response = {"reply": "I'm sorry, I couldn't understand that. Can you ask me something else?"}

#     if user_message:
#         response["reply"] = f"You said: {user_message}. How can I assist you?"

#     return jsonify(response)

