from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import webbrowser

bot =ChatBot('Bot')
trainer=ListTrainer(bot)
import logging
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)


for files in os.listdir('C:\Users\chandu\Desktop\ai_project'):
    data= open('C:\Users\chandu\Desktop\ai_project'+files,'r').readlines()
    trainer.train(data)

while True:
    message=input('You:')

    if message.strip()!='Bye':
        reply=bot.get_response(message)
        print('TARZ :',reply)

    if message.strip()=='Bye':
        print('TARZ :Bye')
        break
