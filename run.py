# -*- coding: utf-8 -*-
import json
import os
import telebot

from util.log_helper import log
from dialog.engine import DialogEngine


def init():
    global bot
    global dialog_engine

    dialog_engine = DialogEngine()

    telegram_api_key = os.environ.get('TOKEN')
    bot = telebot.TeleBot(telegram_api_key)

init()

@bot.message_handler(func=lambda m: True)
def lambda_handler(event):
    try:
        log('Event: ' + str(event))
        body = json.loads(event['body'])
        message = telebot.types.Message.de_json(body['message'])
        answer = dialog_engine.choose_answer(message)
        bot.reply_to(message, answer)

    except Exception as e:
        log('Error: ' + str(e))

    return {
        'statusCode': 200,
        'body': str(event),
        'headers': {
            'Content-Type': 'application/json'
        }
    }

bot.polling()

