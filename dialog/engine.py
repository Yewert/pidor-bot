import random
import re
import logging
from telebot.types import Message
from dialog.answers import data, tatar_data, photo_answers
from itertools import chain


logger = logging.getLogger(__name__)

class DialogEngine(object):

    @staticmethod
    def choose_answer(message):
        text = None
        if type(message) == str:
            text = message
        elif type(message) == Message:
            if 'zarix908' in message.from_user.username:
                return DialogEngine.chose_answer_for_tatarin(message)
            text = message.text

        for question, answers in data.items():
            if re.match(question, text):
                return random.choice(answers)
        return None

    @staticmethod
    def chose_answer_for_tatarin(message):
        if message.photo:
            return random.choice(photo_answers)
        for question, answers in chain(tatar_data.items(), data.items()):
            if re.match(question, message.text):
                return random.choice(answers)
        return None
