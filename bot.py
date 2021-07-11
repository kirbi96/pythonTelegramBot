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

    bot.send_message(message.chat.id,"Добро пожаловать, {0.first_name}!".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def m(message):
    if message.chat.type == 'private':
        if message.text == '🤵 Связаться с администратором':
            bot.send_message(message.chat.id, 'Администратор ответит вам в течении 5 минут')
        elif message.text == '🕵️‍♀ Посмотреть товар':
            markup = types.InlineKeyboardMarkup()

            markup.row(types.InlineKeyboardButton("Испарители", callback_data='evaporator'))
            markup.row(types.InlineKeyboardButton("Фирменные табаки", callback_data='tobacco'))
            markup.row(types.InlineKeyboardButton("Зажигалки", callback_data='lighter'))

            bot.send_message(message.chat.id, 'Что именно вас интересует?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
    bot.send_message(message.chat.id, message.text)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_inline(call):
        try:
            if call.message:
                if call.data == 'evaporator':
                    markup = types.InlineKeyboardMarkup(row_width=3)
                    item1 = types.InlineKeyboardButton("Испарители марка 1", callback_data='evaporator1')
                    item2 = types.InlineKeyboardButton("Испарители марка 2", callback_data='evaporator2')
                    item3 = types.InlineKeyboardButton("Испарители марка 3", callback_data='evaporator3')

                    markup.add(item1, item2, item3)

                    bot.send_message(message.chat.id, 'Выберите нужный испаритель?', reply_markup=markup)
                elif call.data == 'tobacco':

                    markup = types.InlineKeyboardMarkup(row_width=3)
                    item1 = types.InlineKeyboardButton("Табак марка 1", callback_data='tobacco1')
                    item2 = types.InlineKeyboardButton("Табак марка 2", callback_data='tobacco2')
                    item3 = types.InlineKeyboardButton("Табак марка 3", callback_data='tobacco3')

                    markup.add(item1, item2, item3)

                    bot.send_message(message.chat.id, 'Выберите нужный табак?', reply_markup=markup)

                elif call.data == 'lighter':

                    markup = types.InlineKeyboardMarkup(row_width=3)
                    item1 = types.InlineKeyboardButton("Зажигалка 1", callback_data='lighter1')
                    item2 = types.InlineKeyboardButton("Зажигалка 2", callback_data='lighter2')
                    item3 = types.InlineKeyboardButton("Зажигалка 3", callback_data='lighter3')

                    markup.add(item1, item2, item3)

                    bot.send_message(message.chat.id, 'Выберите нужную зажигалку?', reply_markup=markup)


        except Exception as e:
            print(repr(e))

#RUN
bot.polling(none_stop=True)