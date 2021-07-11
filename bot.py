import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('🕵️‍♀ Посмотреть товар')
    item2 = types.KeyboardButton('🤵 Связаться с администратором')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Добро пожаловать, {0.first_name}'.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

# @bot.message_handler(content_types=['text'])
# def m(message):
#     bot.send_message(message.chat.id, message.text)

#RUN
bot.polling(none_stop=True)