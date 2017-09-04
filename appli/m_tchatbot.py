#!/usr/bin/env python

#manage a small chat box with a robot


from chatterbot import ChatBot

def init():
    chatbot = ChatBot('Ron Obvious', trainer="chatterbot.trainers.ChatterBotCorpusTrainer")
    chatbot.train("chatterbot.corpus.english")
    return chatbot

def tchat(message, chatbox):
    print message
    return chatbox.get_response(message)
