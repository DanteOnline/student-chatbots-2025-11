import logging

from aiogram import F, Router, types

from app.models import llm_client
from app.services.voice import (
    text_to_audio,
    transcribe_with_fallback,
)

logger = logging.getLogger('bot')

router = Router()


async def create_filepath(message: types.Message) -> str:
    """
    Получаем путь для хранения пользовательских сообщений
    :param message: сообщение пользователя
    :return: путь в формате str
    """
    user_id = message.from_user.id
    return f'./voice_messages/user_{user_id}'

async def create_output_path(message: types.Message) -> str:
    """
    Получаем путь для хранения ответов пользователю
    :param message: сообщение пользователя
    :return: путь в формате str
    """
    user_id = message.from_user.id
    return f'./voice_replies/user_{user_id}.wav'


async def download_file(message: types.Message) -> str | None:
    """
    Скачиваем голосовое сообщение
    :param message: сообщение пользователя
    :return: путь скаченного файла в формате str
    """
    filepath = await create_filepath(message)
    await message.bot.download(
        message.voice,
        filepath
    )
    return filepath


@router.message(F.voice)
async def on_voice(message: types.Message) -> None:
    """
    Обработка голосового сообщения
    :param message: сообщение пользователя
    :return: None
    """
    # скачиваем голосовое сообщение
    filepath = await download_file(message)

    # получаем текст голосового сообщения
    text, lang, error_message = transcribe_with_fallback(
        audio_path=filepath,
        language='ru',
    )

    # возвращаем ошибку если транскрибция не удалась
    if error_message:
        input_text = error_message
        await message.answer(input_text)
        return

    # Возвращаем текст сообщения (от пользователя)
    input_text = text
    await message.answer(input_text)

    max_text_length = 500
    if len(input_text) > max_text_length:
        await message.answer("Слишком серьёзная проблема. Я такое не потяну.")
        return

    # Задаем вопрос llm
    thinking = await message.answer("Думаю...")
    answer = await llm_client.ask(input_text)
    # Отвечаем текстом
    await thinking.edit_text(answer)

    # Переводим текст в голос
    output_path = await create_output_path(message)
    output_path, current_speaker = await text_to_audio(answer, output_path)

    # Отвечаем пользователю голосом
    audio_file = types.FSInputFile(output_path)

    await message.bot.send_document(
        chat_id=message.chat.id,
        document=audio_file,
        caption=f"Отвечает {current_speaker}"
    )
