import asyncio

from app.strategies.keywords import keywords_strategy

result = asyncio.run(
    keywords_strategy('Где жил Гарри Поттер?')
)

print(result)
