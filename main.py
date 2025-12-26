"""
Entrypoint для запуска бота
"""
import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, ForceReply

from config import BOT_TOKEN
from app.keyboars.reply import (
    main_menu_keyboard,
    ABOUT_BUTTON_TEXT,
    FAQ_BUTTON_TEXT,
    FORM_BUTTON_TEXT,
)
from app.keyboars.inline import (
    faq_keyboard,
    WHO_CREATOR,
    WHO_TEACHER,
)

dp = Dispatcher()


@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    """
    Обработчик команды /start
    """
    text = ('Привет, я бот - результат домашнего задания по курсу OTUS. '
            'Юзай меню внизу или команды /start, /help для навигации. ')
    await message.answer(text, reply_markup=main_menu_keyboard)


@dp.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    """
    Обработчик команды /help
    """
    text = ('Привет, я бот - результат домашнего задания по курсу OTUS. '
            'Юзай меню внизу или команды /start, /help для навигации. ')
    await message.answer(text, reply_markup=main_menu_keyboard)


@dp.message(F.text == ABOUT_BUTTON_TEXT)
async def about_text_handler(message: Message) -> None:
    """
    Обработчик ввода "О нас"
    """
    text = '<i>Этот</i> бот был создан для домашнего задания курса <b>OTUS.</b>'
    await message.answer(text, parse_mode='HTML')


@dp.message(F.text == FAQ_BUTTON_TEXT)
async def faq_text_handler(message: Message) -> None:
    """
    Обработчик ввода "FAQ"
    """
    text = 'Часто задаваемые вопросы:'
    await message.answer(text, reply_markup=faq_keyboard)


@dp.callback_query(F.data.in_({WHO_CREATOR, WHO_TEACHER}))
async def on_ask_inline_button_click(callback: CallbackQuery):
    """
    Выбор FAQ вопроса
    """
    action = callback.data or ''
    if action == WHO_CREATOR:
        await callback.message.answer('юный падаван, Леонид')
        return
    if action == WHO_TEACHER:
        await callback.message.answer('Великий Магистр, Станислав')
        return
    await callback.message.answer('Неизвестная кнопка')


# FSM

class FormChoice(StatesGroup):  # pylint:disable=too-few-public-methods
    """
    Стадии заполнения анкеты
    """
    name = State()
    city = State()


@dp.message(F.text == FORM_BUTTON_TEXT)
async def form_start(message: Message, state: FSMContext):
    """
    Начало заполнение анкет, запрос имени
    """
    await state.clear()
    await state.set_state(FormChoice.name)
    # force reply
    await message.answer('Как вас зовут: ', reply_markup=ForceReply())


@dp.message(FormChoice.name)
async def name_enter(message: Message, state: FSMContext):
    """
    Пользователь ввел имя
    """
    name = message.text
    await state.update_data(name=name)
    await state.set_state(FormChoice.city)
    await message.answer('Ваш город проживания: ', reply_markup=ForceReply())


@dp.message(FormChoice.city)
async def city_enter(message: Message, state: FSMContext):
    """
    Пользователь ввел город
    """
    city = message.text
    data = await state.get_data()
    name = data.get('name')
    result_text = f'Привет {name} из {city}'
    await message.answer(result_text, reply_markup=main_menu_keyboard)
    await state.clear()

# END FSM

async def main() -> None:
    """
    Запуск бота
    """
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
