# """
# Пакет DB
# """
#
# from .models import Base
# from .session import engine
#
#
# async def init_db():
#     """
#     Создание базы данных
#     """
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
