"""
Inline клавиатуры (в сообщениях)
"""
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


WHO_CREATOR = 'who_creator'
WHO_TEACHER = 'who_teacher'

who_creator = InlineKeyboardButton(text='Кто сделал этого бота?', callback_data=WHO_CREATOR)
who_teacher = InlineKeyboardButton(text='Кто научил делать ботов?', callback_data=WHO_TEACHER)

keyboard_rows_ask = [
    [who_creator],
    [who_teacher],
]

faq_keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_rows_ask)
