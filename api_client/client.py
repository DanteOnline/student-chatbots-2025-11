import asyncio
import httpx
from django.conf import settings
from . import errors


async def is_not_found_status(status: int) -> bool:
    """
    Страница не найдена 404
    :param status: код статуса
    :return:
    """
    return status == 404


async def is_retry_status(status: int) -> bool:
    """
    Статус при котором нужно делать retry
    :param status: код статуса
    """
    return status in (408, 429, 500, 502, 503, 504)


async def get_json_dict(
        url: str,
        attempts: int = int(settings.MAX_RETRY_ATTEMPTS),
        timeout: int = int(settings.DEFAULT_TIMEOUT),
) -> tuple[bool, list | dict, str]:
    """
    :param url: адрес в api
    :param attempts: количество попыток переподключения
    :param timeout: время ожидания
    :return: [успех, словарь ответа, текст ошибки]
    """
    last_error: Exception | None = None
    attempts = attempts + 1

    async with httpx.AsyncClient(timeout=timeout) as client:
        for attempt in range(1, attempts + 1):
            try:
                response = await client.get(url)
                response.raise_for_status()
                payload = response.json()
                if isinstance(payload, list):
                    return True, payload, ''
                # raise ApiClientError("Expected JSON object in response")
                return False, {}, 'Неправильный ответ от API'
            except httpx.TimeoutException as err:
                last_error = errors.ApiClientTimeoutError(str(err))
            except httpx.HTTPStatusError as err:
                status = err.response.status_code

                if await is_not_found_status(status):
                    return False, {}, 'Название страны не найдено'

                try:
                    message = err.response.text
                except Exception:
                    message = "No response body"
                if await is_retry_status(status) and attempt < attempts:
                    last_error = errors.ApiClientHttpError(status, message)
                else:
                    # raise ApiClientHttpError(status, message) from err
                    return False, {}, f'Ошибка API {message}'
            except httpx.RequestError as err:
                last_error = errors.ApiClientNetworkError(str(err))

            if attempt < attempts:
                await asyncio.sleep(timeout)

        if last_error is not None:
            # raise last_error
            try:
                raise last_error
            except Exception as e:
                return False, {}, str(e)
        # raise ApiClientError("Unknown API client error")
        return False, {}, 'Неизвестная ошибка API'
