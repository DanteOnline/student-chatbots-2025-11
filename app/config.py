"""
Настройки проекта
"""

from os import getenv

from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = getenv('BOT_TOKEN')
# Тут надо будет разрулить когда добавить postgres, пока использую 2 константы
# для работы и для alembic
DATABASE_URL = getenv('DATABASE_URL', 'sqlite+aiosqlite:///./data/db.sqlite3')
SYNC_DATABASE_URL = getenv('DATABASE_URL', 'sqlite:///./data/db.sqlite3')
# Для webhook
WEBHOOK_URL = getenv("WEBHOOK_URL")  # Базовый URL вебхука
WEBHOOK_PATH = getenv("WEBHOOK_PATH", "/webhook")  # Путь для webhook
WEBHOOK_HOST = getenv("WEBHOOK_HOST", "localhost")  # Хост для FastAPI сервера
WEBHOOK_PORT = int(getenv("WEBHOOK_PORT", "8000"))  # Порт для FastAPI сервера
