from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder


menu_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Sherik kerak"),
            KeyboardButton(text="Ish joyi kerak"),
        ],
        [
            KeyboardButton(text='Hodim kerak'),
            KeyboardButton(text='Ustoz kerak'),
        ],
        [
            KeyboardButton(text='Shogird kerak'),
            KeyboardButton(text="O'quv markaz"),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Kanalga e'lon berish uchun kerakli tugmani bosing..."
)
