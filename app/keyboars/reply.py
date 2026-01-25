"""
Reply клавиатуры (в чате)
"""

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

FAQ_BUTTON_TEXT = 'FAQ'
ABOUT_BUTTON_TEXT = 'О нас'
FORM_BUTTON_TEXT = 'Анкета'


faq_button = KeyboardButton(text=FAQ_BUTTON_TEXT)
about_button = KeyboardButton(text=ABOUT_BUTTON_TEXT)
form_button = KeyboardButton(text=FORM_BUTTON_TEXT)


main_menu_layout = [
    [faq_button, about_button, form_button],
]

main_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=main_menu_layout,
    resize_keyboard=True,
)
