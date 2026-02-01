"""
Пакет app
"""

import logging

from aiogram import Dispatcher

from app.handlers import (
    about,
    common,
    errors,
    faq,
    form,
)
from app.middlewares.logging import LoggingMiddleware

logging.basicConfig(
    level=logging.INFO,
    format=('%(asctime)s | %(levelname)s | %(name)s | %(message)s'),
)

logger = logging.getLogger('bot')


async def init_dispatcher() -> Dispatcher:
    """
    Настройка Dispatcher
    """
    dispatcher = Dispatcher()
    # middlewares
    dispatcher.message.middleware(LoggingMiddleware())
    dispatcher.callback_query.middleware(LoggingMiddleware())

    # routers
    # для ошибок
    dispatcher.include_router(errors.router)
    # основные
    dispatcher.include_router(common.router)
    dispatcher.include_router(about.router)
    dispatcher.include_router(faq.router)
    dispatcher.include_router(form.router)
    return dispatcher
