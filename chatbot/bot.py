import spacy
from chatbot.intents import INTENT_KEYWORDS
from chatbot.responses import RESPONSES

class ChatBot:
    def __init__(self):
        self.nlp = spacy.load('es_core_news_md')

    def get_intent(self, user_input):
        for intent, keywords in INTENT_KEYWORDS.items():
            if any(keyword in user_input for keyword in keywords):
                return intent
        return "default"

    def get_response(self, intent):
        return RESPONSES.get(intent, RESPONSES["default"])

    def chat(self):
        print("Hola, soy tu asistente para funciones básicas del celular. ¿En qué puedo ayudarte hoy?")
        while True:
            user_input = input("Tú: ").lower()
            intent = self.get_intent(user_input)
            response = self.get_response(intent)
            print("Asistente:", response)
            if intent == "despedida":
                break
