"""
Настройки проекта
"""
from __future__ import annotations

from os import getenv

from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = getenv('BOT_TOKEN')

# Для webhook
WEBHOOK_URL = getenv("WEBHOOK_URL")  # Базовый URL вебхука
WEBHOOK_PATH = getenv("WEBHOOK_PATH", "/webhook")  # Путь для webhook
WEBHOOK_HOST = getenv("WEBHOOK_HOST", "localhost")  # Хост для FastAPI сервера
WEBHOOK_PORT = int(getenv("WEBHOOK_PORT", "8000"))  # Порт для FastAPI сервера

# Пути
DOCS_DIR = "./docs"

# Эмбеддинги; переменные в .env
EMBEDDING_BASE_URL = getenv("BASE_URL", "http://localhost:1234/v1")
EMBEDDING_MODEL = getenv("EMBEDDING_MODEL", "local")
EMBEDDING_API_KEY = getenv("EMBEDDING_API_KEY", "some key")

# Индексация: батчи и чанкование
EMBEDDING_BATCH_SIZE = int(getenv("EMBEDDING_BATCH_SIZE", "100"))
CHUNK_SIZE = int(getenv("CHUNK_SIZE", "500"))
CHUNK_OVERLAP = int(getenv("CHUNK_OVERLAP", "50"))

# Qdrant
QDRANT_HOST = getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = int(getenv("QDRANT_PORT", "6333"))
QDRANT_COLLECTION = getenv("QDRANT_COLLECTION", "documents")
QDRANT_UPSERT_BATCH_SIZE = int(getenv("QDRANT_UPSERT_BATCH_SIZE", "100"))

# Поиск (RAG)
SEARCH_TOP_K = int(getenv("SEARCH_TOP_K", "15"))
SCORE_THRESHOLD = float(getenv("SCORE_THRESHOLD", "0.5"))
