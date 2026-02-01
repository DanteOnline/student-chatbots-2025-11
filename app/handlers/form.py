"""
Раздел Анкета
"""

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ForceReply, Message

from app.db.repository import get_person_list, save_person
from app.db.session import session_cls
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
    person_form = create_person_form(name, city, message.from_user.id)
    async with session_cls() as session:
        person = await save_person(session, person_form)
    result_text = (
        f'Спасибо {person.name} из {person.city}. '
        f'Ваши данные были сохранены в базу. '
        'Вы можете их посмотреть командой /history'
    )
    await message.answer(result_text, reply_markup=main_menu_keyboard)
    await state.clear()


@router.message(Command('history'))
async def command_start_handler(message: Message) -> None:
    """
    Обработчик команды /history
    """
    async with session_cls() as session:
        person_list = await get_person_list(
            session,
            message.from_user.id,
        )

    response_text = '\n'.join([str(person) for person in person_list])
    await message.answer(response_text, reply_markup=main_menu_keyboard)
