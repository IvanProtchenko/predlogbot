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

@bot.message_handler(func=lambda message: True, content_types=['photo','audio', 'video', 'document', 'text', 'location', 'contact', 'sticker'])
def all_messages(message):
    #print(str(message))
    bot.reply_to(message, 'Сообщение принято')
    bot.forward_message(GROUP_ID, message.chat.id, message.message_id)

if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
    except:
        print('ошибка')