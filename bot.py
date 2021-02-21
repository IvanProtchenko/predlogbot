import telebot
from telebot import types
import os

#Настройки бота
TOKEN=os.environ['TOKEN'] 
bot = telebot.TeleBot(TOKEN)
GROUP_ID=os.environ['GROUP_ID']
HELLO_MSG=os.environ['HELLO_MSG']

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, HELLO_MSG)

@bot.message_handler(commands=['id'])
def id(message):
    bot.reply_to(message,message.chat.id)

@bot.message_handler(func=lambda message: True, content_types=['photo','audio', 'video', 'document', 'text', 'location', 'contact', 'sticker','voice'])
def all_messages(message):
    if str(message.chat.id) != str(GROUP_ID):
        bot.forward_message(GROUP_ID, message.chat.id, message.message_id)
    else:
        bot.send_message(message.from_user.id, message.text )

if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
    except:
        print('ошибка')

