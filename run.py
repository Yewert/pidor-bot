import os
import telebot

from dialog.engine import DialogEngine

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)


dialog_engine = DialogEngine()

telegram_api_key = os.environ.get('TOKEN')
bot = telebot.TeleBot(telegram_api_key)


@bot.message_handler(func=lambda m: True)
def lambda_handler(event):
    try:
        if event.content_type != 'text':
            logger.debug(event)
        answer = dialog_engine.choose_answer(event)
        if answer:
            bot.reply_to(event, answer)

    except Exception as e:
        logger.error(e)


bot.polling()

