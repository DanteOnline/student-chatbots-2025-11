"""
Раздел Анкета
"""
from aiogram import Router, F
from aiogram.types import Message, ForceReply
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from app.keyboars.reply import FORM_BUTTON_TEXT, main_menu_keyboard
from app.models import create_person_form


router = Router()

class FormChoice(StatesGroup):  # pylint:disable=too-few-public-methods
    """
    Стадии заполнения анкеты
    """
    name = State()
    city = State()


@router.message(F.text == FORM_BUTTON_TEXT)
async def form_start(message: Message, state: FSMContext):
    """
    Начало заполнение анкет, запрос имени
    """
    await state.clear()
    await state.set_state(FormChoice.name)
    await message.answer('Как вас зовут: ', reply_markup=ForceReply())


@router.message(FormChoice.name)
async def name_enter(message: Message, state: FSMContext):
    """
    Пользователь ввел имя
    """
    name = message.text
    await state.update_data(name=name)
    await state.set_state(FormChoice.city)
    await message.answer('Ваш город проживания: ', reply_markup=ForceReply())


@router.message(FormChoice.city)
async def city_enter(message: Message, state: FSMContext):
    """
    Пользователь ввел город
    """
    city = message.text
    data = await state.get_data()
    name = data.get('name')
    person_form = create_person_form(name, city)
    result_text = f'Привет, {person_form}'
    await message.answer(result_text, reply_markup=main_menu_keyboard)
    await state.clear()
