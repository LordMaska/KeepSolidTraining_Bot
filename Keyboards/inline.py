from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


from Callbacks.pagination import Paginator


def tren_pag(page: int=0):
    builder=InlineKeyboardBuilder()
        
    builder.button(text='Назад', callback_data=Paginator(action='prev', page=page).pack()),
    builder.button(text='Далі', callback_data=Paginator(action='next', page=page).pack())
    builder.adjust(2)
    return builder.as_markup()