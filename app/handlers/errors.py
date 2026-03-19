"""
Обработка ошибок
"""

import logging

from aiogram import Router
from aiogram.types import ErrorEvent

logger = logging.getLogger('bot')

router = Router()


@router.errors()
async def error_handler(event: ErrorEvent) -> None:
    """
    Централизованное логирование ошибок
    """
    logger.exception(
        'Unhandled error: %s',
        event.exception,
    )
