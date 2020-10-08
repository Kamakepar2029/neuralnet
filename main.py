# -*- coding: utf-8 -*-
import telebot
import config
import neural
import subprocess
import os
import sys
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def kolya(message):
  bot.send_message(message.chat.id, 'Привет 😊, Я не бот 🤖.')
  bot.send_message(message.chat.id, '😌 Спроси абсолютно все что угодно. Общайся со мной.')
  bot.send_message(message.chat.id, '❔ Я отвечу на любой твой вопрос. Иногда мои ответы могут быть не связаны, но это нормально. Я тупой.')

@bot.message_handler(content_types=['text'])
def lalala(message):
  fullstring = open("admins.txt", "r").read()
  if (message.text == 'Привет'):
    bot.send_message(message.chat.id, 'Привет. Как дела?')
  else:
    if (str(message.chat.id) in fullstring): 
      if ('?') in message.text:
        loln = neural.add_phrase(message.text,True,q)
        bot.send_message(message.chat.id, loln)
      else:
        loln = neural.add_phrase(message.text,True,a)
        bot.send_message(message.chat.id, loln)
    else:
      if ('?') in message.text:
        loln = neural.add_phrase(message.text,False,q)
        bot.send_message(message.chat.id, loln)
      else:
        loln = neural.add_phrase(message.text,False,a)
        bot.send_message(message.chat.id, loln)
bot.polling(none_stop=True)
