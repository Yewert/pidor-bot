import os
import telebot

from telebot.types import Message
from dialog.engine import DialogEngine

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO, filename='bot.log')
logger = logging.getLogger(__name__)


dialog_engine = DialogEngine()

telegram_api_key = os.environ.get('TOKEN')
bot = telebot.TeleBot(telegram_api_key)


@bot.message_handler(func=lambda m: True)
def lambda_handler(message):
    try:
        if type(message) is not Message:
            logger.warning(type(message))
        if message.content_type != 'text':
            logger.info(message)
        answer = dialog_engine.choose_answer(message)
        if answer:
            bot.reply_to(message, answer)

    except Exception as e:
        logger.warning(e)


while True:
    try:
        bot.polling()
    except Exception as e:
        logger.error(e)
