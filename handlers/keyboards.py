from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo


def inline_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text='text', callback_data='data'),
            InlineKeyboardButton(text='text1', callback_data='data1')
        ],
        [InlineKeyboardButton(text='text2', callback_data='data2')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def reply_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text='text1')],
        [KeyboardButton(text='text2')]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


def inline_webapp_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text='text', web_app=WebAppInfo(url='url'))]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
