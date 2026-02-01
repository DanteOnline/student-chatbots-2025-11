import logging
from contextlib import asynccontextmanager

from aiogram import Bot
from aiogram.types import Update
from app import config, init_dispatcher
from fastapi import FastAPI, Request, Response, status

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=config.BOT_TOKEN)

async def setup_webhook():
    webhook_url = f'{config.WEBHOOK_URL}{config.WEBHOOK_PATH}'
    """Установка webhook в Telegram."""
    if not webhook_url:
        raise RuntimeError("WEBHOOK_URL not set. Проверьте .env файл")


    await bot.set_webhook(webhook_url)
    logger.info(f"Webhook установлен: {webhook_url}")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifecycle events для FastAPI."""
    dispatcher = await init_dispatcher()
    app.state.dispatcher = dispatcher
    # Startup
    await setup_webhook()
    yield
    # Shutdown
    await bot.session.close()


# FastAPI приложение с lifespan
app = FastAPI(title="Telegram Bot Webhook", lifespan=lifespan)


@app.post(config.WEBHOOK_PATH)
async def webhook_handler(request: Request):
    """Обработчик webhook от Telegram."""
    try:
        update_data = await request.json()
        update = Update(**update_data)
        dispatcher = app.state.dispatcher
        await dispatcher.feed_update(bot, update)
        return Response(status_code=status.HTTP_200_OK)
    except Exception as e:
        logger.exception(f"Webhook error: {e}")
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.get("/health")
async def health_check():
    """Health-check endpoint."""
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    # Запуск FastAPI сервера
    # lifespan будет вызван автоматически при старте и остановке
    uvicorn.run(
        app,
        host=config.WEBHOOK_HOST,
        port=config.WEBHOOK_PORT,
    )
