import telebot
from requests import get

bot = telebot.TeleBot('6020603448:AAHV_ecPk8QqspQ8xMFX_6xVKzEqYyMXqV8')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я бот! Я умею искать информацию в интернете за тебя. Напиши свой запрос в сообщении ниже.')

@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_message(message.chat.id, 'вот твоя ссылка: ' +  "https://google.com/?q=" + message.text)

bot.polling()