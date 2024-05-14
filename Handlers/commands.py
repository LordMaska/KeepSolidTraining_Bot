from aiogram import Router, F
from aiogram.types import Message, FSInputFile, URLInputFile
from aiogram.filters import CommandStart, Command

from Keyboards import reply, inline
from Data.subloader import get_tren

router = Router()

# Команда /start
@router.message(CommandStart())
async def start(message: Message):
    start_photo=FSInputFile('Trening_bot/Data/start.jpg')
    await message.answer_photo( photo=start_photo,
        caption=f'''Вітаю, <b>{message.from_user.first_name}!</b>\n
Я - Чат-бот компанії <b>\"KeepSolid\"</b>, необхідний для зручного ознайомлення із нею, її тренінгами та швидкого запису на ці самі тренінги.\n 
Для однієї із цих дій, натисніть на відповідну кнопку під вашим полем вводу👇''',
        reply_markup=reply.main)

# Команда кнопки "Про нас"
@router.message(F.text == 'Про нас')
async def about(message: Message):
        about_photo=FSInputFile('Trening_bot/Data/About_us.jpg')
        await message.answer_photo(photo=about_photo,
                                   caption='''
<b>Переговори як вони є</b>
<b>Тренінг особистих переговорних навичок</b>
<i>Базовий тренінг для людей, яки хочуть відпрацювати свою поведінку на різних етапах переговорів: від подготовки до оформлення домовленостей.</i>
<i>Спочатку знайомимось з технікою чи прийомом, потім відпрацьовуємо їх в групі, виконуючи вправи, а потім вже в режимі симуляцій справжніх переговорів закріпляємо, виконуючи різні кейси.</i>''', 
                                    reply_markup=reply.main)
        
# Команда кнопки "Тренінги"
@router.message(F.text == 'Тренінги')
async def trening(message: Message):
    
    tren=await get_tren('name')
    about=await get_tren('about')
    photo_tren=await get_tren('Photo')
    
    await message.answer_photo(photo=photo_tren[0],
caption=f'''<B>{tren[0]}</B>\n
{about[0]}''', 
        reply_markup=inline.tren_pag())