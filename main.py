from config import DEFAULT_TIMEOUT
from core.fetch_demo import get_info


if __name__ == '__main__':
    request_data = [
        {
            'url': 'https://example.com',
            'fields': [],
        },
        {
            'url': 'https://example.com',
            'fields': [],
        },
    ]
    get_info(
        request_data,
        DEFAULT_TIMEOUT,
    )
