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
  if (message.text == 'Привет'):
    bot.send_message(message.chat.id, 'Привет. Как дела?')
  else:
    loln = neural.add_phrase(message.text)
    bot.send_message(message.chat.id, loln)
bot.polling(none_stop=True)
