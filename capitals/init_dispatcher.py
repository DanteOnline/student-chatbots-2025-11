from aiogram import Dispatcher
from . import handlers


async def init_dispatcher() -> Dispatcher:
    """
    Настройка Dispatcher
    """
    dispatcher = Dispatcher()
    # основные
    dispatcher.include_router(handlers.router)
    return dispatcher
