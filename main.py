# -*- coding: utf-8 -*-
import telebot
import config
import neural
import subprocess
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def kolya(message):
  bot.send_message(message.chat.id, 'Hello 😊, I am not a bot 🤖.')
  bot.send_message(message.chat.id, '😌 Ask me everything you want.')
  bot.send_message(message.chat.id, '❔ I will answer every your question.')

@bot.message_handler(content_types=['text'])
def lalala(message):
  if (message.text == 'Hello'):
    bot.send_message(message.chat.id, 'Hello Man')
  else:
    loln = add_phrase(message.text)
    bot.send_message(message.chat.id, loln)
bot.polling(none_stop=True)
