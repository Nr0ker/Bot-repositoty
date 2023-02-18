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

@bot.message_handler(commands=['start'])
def startFunc(message):
    bot.send_message(message.chat.id, 'Що ви хочете зробити?', reply_markup=buttonses())
    print(message.text)

def appending_lis(list:list, apendment):
    list.append(apendment)
    return list

@bot.message_handler(content_types=['text'])
def get_user_info(message):
    if message.text == "Введіть мультик який хочете додати:":
        info = message.text
        appending_lis(list_for_cartoons, info)
        print(list_for_cartoons)
        print(info)

        return info

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'додавання':
        bot.send_message(call.from_user.id, 'Введіть мультик який хочете додати:')
        print(list_for_cartoons)
    if call.data == 'показати список':
        bot.send_message(call.from_user.id, f'Ось весь список мультиків {list_for_cartoons}')

bot.polling(none_stop=True)