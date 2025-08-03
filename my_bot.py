
from dotenv import load_dotenv
import os
import json
import random
import telebot
import time

load_dotenv()
ADMINS_ID=json.loads(os.getenv('ADMINS_ID'))
API_Token=(os.getenv('API_TOKEN'))

print(os.getenv('start_message'))

bot = telebot.TeleBot(API_Token)

answers = [
    "Да", "Нет", "Возможно", "Вероятнее всего", "Сомневаюсь", "Определенно нет",
    "Конечно", "Маловероятно", "Сложно сказать", "Скорее всего да"
]

@bot.message_handler(content_types=['text'])
def send_prediction(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(1)
    prediction = random.choice(answers)
    bot.reply_to(message, prediction)

# Запускаем бота
bot.infinity_polling()
