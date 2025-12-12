import asyncio
from config import DEFAULT_TIMEOUT
from core.fetch_demo import get_capitals


if __name__ == '__main__':
    country_list = [
        'Russia',
        'Georgia',
        'Turkey',
    ]
    asyncio.run(
        get_capitals(
            country_list,
            DEFAULT_TIMEOUT,
        )
    )
