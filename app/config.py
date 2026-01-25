"""
Настройки проекта
"""

from os import getenv

from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = getenv('BOT_TOKEN')
# Тут надо будет разрулить когда добавить postgres, пока использую 2 константы
# для работы и для alembic
DATABASE_URL = getenv('DATABASE_URL', 'sqlite+aiosqlite:///./db.sqlite3')
SYNC_DATABASE_URL = getenv('DATABASE_URL', 'sqlite:///./db.sqlite3')
