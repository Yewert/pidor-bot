# -*- coding: utf-8 -*-
data = {
    r'(?i)^привет\W*$': [
        'ну привет',
        'тебя не звали, иди отсюда'
    ],
    r'(?i)^пока\W*$': [
        'ну пока',
        'ну и пиздуй'
    ],
    r'(?i)^пизда\W*$': [
        'не ругайся!'
    ],
    r'(?i)^да\W*$': [
        'манда',
        'хуй на'
    ],
    r'(?i)^нет\W*$': [
        'пидора ответ'
    ],
    r'(?i)(\w*\s)?пид[о?]р\w*$': [
        'пидор дед твой',
        'ты сам пидор'
    ],
    r'(?i)^сид[о?]р\W*$': [
        'это я люблю'
    ],
    r'(?i)^го': [
        'го по пиву лучше '
    ],
    r'(?:[^(]*\))|(?:.*\)\))\W*$': [
        '))))))))))))',
        'гы))))'
    ],
    r'(?i)^кто хостит бота?': [
        'царь и бог @yewert'
    ],
    r'(?i)^хуйня':[
        'причем та еще!'
    ]
}

tatar_data = {
    r'(?i)не смешно': [
        'уууу нисмищно сложна ыыыы'
    ],
    r'(?i)^аа+^':[
        'вот это поворот даааа?'
    ],
    r'(?i)конечно':[
        'хуечно'
    ],
    r'(?i)(ах){2,}':[
        'апхапахпхапхапвахпхапвап'
    ]
}

photo_answers = [
    'опять древний мем скинул?',
    'опять что-то не смешное?'
]
