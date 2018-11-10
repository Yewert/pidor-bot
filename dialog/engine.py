import random
import re

from telebot.types import Message
from dialog.answers import data, tatar_data, photo_answers
from util.log_helper import log
from itertools import chain


class DialogEngine(object):
    def __init__(self):
        log('Answers data:')
        for question, answers in data.items():
            log(question + ' -> ' + str(answers))

    @staticmethod
    def choose_answer(message):
        text = None
        if type(message) == str:
            text = message
        elif type(message) == Message:
            log(message.from_user.username)
            text = message.text

        log('Message text: ' + str(text))
        for question, answers in data.items():
            if re.match(question, text):
                return random.choice(answers)
        return None

    @staticmethod
    def chose_answer_for_tatarin(message):
        if message.content_type == 'photo':
            return random.choice(photo_answers)
        for question, answers in chain(tatar_data.items(), data.items()):
            if re.match(question, message.text):
                return random.choice(answers)
        return None
