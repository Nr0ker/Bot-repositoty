from copy import copy

import telebot
import random
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot('5988465298:AAG9vcEVtgYlDyiTloFDTc-6xLjR2245ri0')
list_for_cartoons = []

def buttonses():
    markupqq = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("Додати мультик", callback_data="додавання")
    button2 = InlineKeyboardButton("Продивитись список всіх мультиків", callback_data="показати список")
    markupqq.add(button1, button2)
    return markupqq

# def appending_lis(apendment):
#     global list_for_cartoons
#     list_for_cartoons.append(apendment)
#     print(list_for_cartoons)
@bot.message_handler(commands=['start'])
def startFunc(message):
    bot.send_message(message.chat.id, 'Що ви хочете зробити?', reply_markup=buttonses())
    print(message.text)

@bot.message_handler(content_types=['text'])
def get_user_info(message):
    global list_for_cartoons
    b = '\n'
    if message.text:
        info = message.text
        list_for_cartoons.append(info)
        print("Це список мультів", list_for_cartoons)
        print("Мульт, який зараз ввели", info)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'додавання':
        msg = bot.send_message(call.from_user.id, 'Введіть мультик який хочете додати:')
        bot.register_next_step_handler(msg, get_user_info)
        # print(list_for_cartoons)
    if call.data == 'показати список':
        bot.send_message(call.from_user.id, str(list_for_cartoons))



bot.polling(none_stop=True)