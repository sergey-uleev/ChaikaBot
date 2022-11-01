from typing import Any
import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup as b

bot = telebot.TeleBot('5475021171:AAEkYwe-tgUwWdbcQGarL4FpQSqIDAAM2KY')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="https://itproger.com/"))
    bot.send_message(message.chat.id, 'Передите на сайт', reply_markup=markup)


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    start = types.KeyboardButton('start')
    website = types.KeyboardButton('website')
    markup.add(start, website)
    bot.send_message(message.chat.id, 'Передите на сайт', reply_markup=markup)


bot.polling(none_stop=True)
