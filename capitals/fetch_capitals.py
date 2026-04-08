from api_client.client import get_json_dict


def parse_json(response_json: dict) -> str:
    """
    Достаем столицу из json словаря
    """
    response_dict = response_json[0]
    capital = response_dict['capital'][0]
    return capital


async def get_capital(country_name: str) -> str:
    url = f'https://restcountries.com/v3.1/name/{country_name}'
    is_good, response_dict, error = await get_json_dict(url)
    if not is_good:
        return error
    capital = parse_json(response_dict)
    return capital
