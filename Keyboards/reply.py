from aiogram.types import (
    ReplyKeyboardMarkup, 
    KeyboardButton,
    ReplyKeyboardRemove
)

# Змінна для видалення клавіатури
rmk=ReplyKeyboardRemove()

# Головне меню
main=ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton(text='Тренінги')
    ],
    [
        KeyboardButton(text='Записатися на тренінг'), 
        KeyboardButton(text='Про нас')
    ]
    ],
    resize_keyboard=True, 
    input_field_placeholder='Головне меню',
    selective=True
)