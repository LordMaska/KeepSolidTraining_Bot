from aiogram.fsm.state import State, StatesGroup

class Form(StatesGroup):
    name=State()
    surname=State()
    age=State()
    phone=State()
    email=State()
    trening=State()
    shedule=State()
    interesting=State()
    confirm=State()
