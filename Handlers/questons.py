# Імпорти модулів
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

# Імпорти з інших файлів проекту
from Utils.states import Form
from Keyboards.reply import rmk, main
from Keyboards.builder import answer
from Data.subloader import get_tren, into_record

# Глобальні змінні
router=Router()
into_text=[]
shedule, tren=[], []

# Обробник для початку запису на тренінг
@router.message(F.text == "Записатися на тренінг")
async def fill_answer(message: Message, state:FSMContext):
    del into_text[:]
    await state.set_state(Form.name)
    await message.answer(
        'Введіть ваше ім\'я або натисніть на кнопку під полем вводу 👇',
        reply_markup=answer(message.from_user.first_name)
    )

# Обробник стану запису імені
@router.message(Form.name)
async def form_name(message: Message, state:FSMContext):
    into_text.append(message.text)
    await state.set_state(Form.surname)
    await message.answer(
        'Введіть ваше прізвище або натисніть на кнопку під полем вводу 👇',
        reply_markup=answer(message.from_user.last_name)
    )

# Обробник стану запису прізвища
@router.message(Form.surname)
async def form_surname(message: Message, state:FSMContext):
    into_text.append(message.text)
    await state.set_state(Form.age)
    await message.answer(
        'Вкажіть, скільки вам років (лише число).',
        reply_markup=rmk
    )

# Обробник стану запису віку
@router.message(Form.age)
async def form_age(message: Message, state:FSMContext):
    if message.text.isdigit():
        into_text.append(int(message.text))
        await state.set_state(Form.phone)
        await message.answer(
            'Введіть ваш номер телефону', 
            reply_markup=rmk)
    else: 
        await message.answer('Будь ласка, введіть лише число!')
    
# Обробник стану запису номеру телефону
@router.message(Form.phone)
async def form_phone_text(message: Message, state:FSMContext):
    into_text.append(message.text)
    await state.set_state(Form.email)
    await message.answer(
        'Введіть адресу вашої електронної пошти.',
        reply_markup=rmk)

# Обробник стану запису електронної пошти
@router.message(Form.email)
async def form_email(message: Message, state:FSMContext):
    into_text.append(message.text)
    await state.set_state(Form.trening)
    global tren
    tren = await get_tren('name')

    await message.answer(
        'На який тренінг ви бажаєте записатись? \nОберіть 1 з доступних для запису під полем вводу 👇',
        reply_markup=answer(tren)
        )

# Обробник стану запису тренінгу
@router.message(Form.trening)
async def form_trening(message: Message, state:FSMContext):
    into_text.append(message.text)
    await state.set_state(Form.shedule)
    global shedule
    shedule=[
            'СБ-НД, з 10:00 до 14:00',
            'СБ, з 10:00 до 18:00',
            'Можу у будні дні, два дні поспіль, 10:00-14:00',
            'Можу у будні дні, один день, 10:00-18:00'
        ]
    await message.answer(
        'Який графік тренувань вам більше підходить? \nОберіть 1 з доступних розкладів під полем вводу 👇',
        reply_markup=answer(shedule)
        )
    
# Обробник для фільтрування тренінгу (в розробці)
'''
@router.message(Form.trening, F.text.casefold().func(lambda message, tren=tren: message.text in tren))
async def incorect_form_trening(message: Message, state:FSMContext):
    await message.answer('Такого тренінгу не існує. Будь-ласка, оберіть існуючий тренінг з варіантів під полем вводу')'''
    
# Обробник стану запису графіка тренувань
@router.message(Form.shedule)
async def form_shedule(message: Message, state:FSMContext):
    into_text.append(message.text)
    await state.set_state(Form.interesting)
    await message.answer(
        'Що саме з теми переговорів вам найбільш цікаво? \nОберіть 1 з доступних під полем вводу 👇 або введіть свій варіант.',
        reply_markup=answer([
            'Особисті навички',
            'Складні переговори',
            'Переговори з партнерами',
            'Переговори в продажах'
        ])
        )

# Обробник для фільтрування графіку тренінгу (в розробці)
'''    
@router.message(Form.shedule, F.text.in_(shedule))
async def incorect_form_trening(message: Message, state:FSMContext):
    await message.answer('Такого графіку тренінгів у нас немає. Будь-ласка, оберіть існуючий графік з варіантів під полем вводу')'''
    
# Обробник стану запису інтересу
@router.message(Form.interesting)
async def form_interesting(message: Message, state:FSMContext):
    into_text.append(message.text)
    await state.set_state(Form.confirm)
    await message.answer(f'''<b>Ви ввели наступні дані для запису на тренінг:</b>\n
Ім\'я: {into_text[0]}
Прізвище: {into_text[1]}
Вік: {into_text[2]} років
Номер телефону: {into_text[3]}
Електронна пошта: {into_text[4]}
Тренінг: {into_text[5]}
Графік тренувань: {into_text[6]}
Цікавитесь: {into_text[7]}

Бажаєте підтвердити режстрацію?''', 
        reply_markup=answer(['Підтвержити', 'Скасувати']))

# Обробник для підтвердження/скасування запису
@router.message(Form.confirm, F.text.in_(['Підтвержити', 'Скасувати']))
async def form_confirm(message: Message, state:FSMContext):
    if message.text == 'Підтвержити':
        await state.clear()
        await into_record(into_text)
        await message.answer('Ви успішно зареєструвались на тренінг. Чекатимемо вас із нетерпінням😊', reply_markup=main)
    else:
        await state.clear()
        await message.answer('Реєстрацію скасовано.', reply_markup=main)

    