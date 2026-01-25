from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)

DATABASE_URL = "sqlite+aiosqlite:///./db.sqlite3"

engine = create_async_engine(
    DATABASE_URL,
    echo=False,
)

SessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)
