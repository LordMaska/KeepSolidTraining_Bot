from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def answer(text: str|list):
    builder = ReplyKeyboardBuilder()
    if isinstance(text, str):
        text=[text]

    [builder.button(text=txt) for txt in text]
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)