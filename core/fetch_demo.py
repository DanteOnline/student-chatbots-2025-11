import asyncio
import httpx


def parse_json(response_json):
    response_dict = response_json[0]
    capital = response_dict['capital'][0]
    return capital


async def get_capital(country_name, timeout):
    url = f'https://restcountries.com/v3.1/name/{country_name}'
    print(f'Ищу столицу страны: {country_name}')
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.get(url)

        response.raise_for_status()
        print(f'Завершили запрос  {url}, статус {response.status_code}')
        response_json = response.json()
        capital = parse_json(response_json)
        return capital
    except httpx.HTTPError as error:
        print(f'Произошла ошибка {error}')
        return ''


async def get_capitals(country_list, timeout):
    print(f'Находим столицы {len(country_list)} стран')
    tasks = [get_capital(country, timeout) for country in country_list]
    print(f'Готово {len(tasks)} задач для запуска')
    responses = await asyncio.gather(*tasks)
    for capital, country in zip(responses, country_list):
        print(f'{country} -> {capital}')
