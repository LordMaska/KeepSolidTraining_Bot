from contextlib import suppress

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters.callback_data import CallbackData

from Keyboards import inline
from Data.subloader import get_tren

router = Router()

class Paginator(CallbackData, prefix='pag'):
    action: str
    page: int


@router.callback_query(Paginator.filter(F.action.in_(["prev","next"])))
async def pag_handler(call:CallbackQuery, callback_data: Paginator):

    tren=await get_tren('name')
    about=await get_tren('about')
    photo_tren=await get_tren('Photo')
    page_num=int(callback_data.page)
    page=page_num-1 if page_num>0 else 0

    if callback_data.action=='next':
        page= page_num+1 if page_num<(len(tren)-1) else page_num

    with suppress(TelegramBadRequest):
        await call.message.delete()
        await call.message.answer_photo(photo=photo_tren[page],
            caption=f'''
<B>{tren[page]}</B>\n
{about[page]}''',
            reply_markup=inline.tren_pag(page)
            )
    await call.answer()