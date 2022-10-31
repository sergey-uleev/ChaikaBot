import telebot

bot = telebot.TeleBot('5475021171:AAEkYwe-tgUwWdbcQGarL4FpQSqIDAAM2KY')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
def get_user_text(message):
    bot.send_message(message.chat.id, message, parse_mode='html')


bot.polling(none_stop=True)
