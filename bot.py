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


# def buttonses():
#   markup = ReplyKeyboardMarkup()
#   buton1 = KeyboardButton('Додати мультик')
#   button2 = KeyboardButton('Показати список всіх мультиків')
#   markup.add(buton1, button2)
#   return markup


# @bot.message_handler(content_types=['text'])
# def get_name(message):
#     name = message.text
#     print(name)

@bot.message_handler(commands=['start'])
def startFunc(message):
    bot.send_message(message.chat.id, 'Що ви хочете зробити?', reply_markup=buttonses())
    print(message.text)

def appending_lis(list:list, apendment):
    list.append(apendment)

# def appending_list(apendment):
#     global list_for_cartoons
#     list_for_cartoons.append(apendment)


@bot.message_handler(content_types=['text'])
def get_user_info(message):
    b = '\n'
    if message.text == "Введіть мультик який хочете додати:":
        info = message.text
        appending_lis(list_for_cartoons, info)
        print(list_for_cartoons)

        return info


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'додавання':
        bot.send_message(call.from_user.id, 'Введіть мультик який хочете додати:')
        # print(call.message)
        print(list_for_cartoons)
    if call.data == 'показати список':
        bot.send_message(call.from_user.id, list_for_cartoons)
    # list_for_cartoons.append(message)


# @bot.message_handler(content_types=['text'])
# def callback_quer(message):
#   if message.text == 'Додати мультик':
#     bot.send_message(message.chat.id, 'Введіть мультик який хочете додати: ', reply_markup=appending_list(message.text))
#     print(list_for_cartoons)
#   if message.text == 'Показати список всіх мультиків':
#     bot.send_message(message.chat.id, reply_markup=appending_list(message.text))
#   # list_for_cartoons.append(message)


bot.polling(none_stop=True)