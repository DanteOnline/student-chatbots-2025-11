"""
Логирование
"""

import logging
from typing import Any, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

logger = logging.getLogger('bot')


class LoggingMiddleware(BaseMiddleware):  # pylint: disable=too-few-public-methods
    """
    Middleware для централизованного логирования
    """

    async def __call__(
        self,
        handler: Callable,
        event: Message | CallbackQuery,
        data: Dict[str, Any],
    ):
        state: FSMContext | None = data.get('state')

        user_id = None
        chat_id = None
        content = None

        if isinstance(event, Message):
            user_id = event.from_user.id
            chat_id = event.chat.id
            content = event.text or event.caption or '<non-text message>'

        elif isinstance(event, CallbackQuery):
            user_id = event.from_user.id
            chat_id = event.message.chat.id
            content = f'callback: {event.data}'

        fsm_state = await state.get_state() if state else None

        logger.info(
            'IN | user=%s chat=%s state=%s content=%s',
            user_id,
            chat_id,
            fsm_state,
            content,
        )

        try:
            result = await handler(event, data)

            logger.info(
                'OUT | user=%s chat=%s state=%s result=success',
                user_id,
                chat_id,
                fsm_state,
            )

            return result

        except Exception:
            logger.exception(
                'ERROR | user=%s chat=%s state=%s',
                user_id,
                chat_id,
                fsm_state,
            )
            raise
