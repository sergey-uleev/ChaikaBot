from typing import Any
import telebot
import requests
from telebot import types
from bs4 import BeautifulSoup 

bot = telebot.TeleBot('5475021171:AAEkYwe-tgUwWdbcQGarL4FpQSqIDAAM2KY')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    weather = types.KeyboardButton('погода')
    courses = types.KeyboardButton('курс валют')
    back = types.KeyboardButton('назад')
    markup.add(weather, courses, back)
    mess = f'Здравствуйте, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u>, \n Выберите что Вас интересует?</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'погода':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        weather1 = types.KeyboardButton('Чайковский')
        weather2 = types.KeyboardButton('Пермь')
        weather3 = types.KeyboardButton('Москва')
        back = types.KeyboardButton('назад')
        markup.add(weather1, weather2, weather3, back)
        bot.send_message(message.chat.id, 'погода', reply_markup=markup)
    elif message.text == 'курс валют':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        courses1 = types.KeyboardButton('USD')
        courses2 = types.KeyboardButton('EUR')
        courses3 = types.KeyboardButton('CNY')
        back = types.KeyboardButton('назад')
        markup.add(courses1, courses2, courses3, back)
        bot.send_message(message.chat.id, 'курс валют', reply_markup=markup)
    elif message.text == 'назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        weather = types.KeyboardButton('погода')
        courses = types.KeyboardButton('курс валют')
        back = types.KeyboardButton('назад')
        markup.add(weather, courses, back)
        bot.send_message(message.chat.id, 'назад', reply_markup=markup)

bot.polling(none_stop=True)

