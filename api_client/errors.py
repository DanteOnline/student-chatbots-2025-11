class ApiClientError(Exception):
    """Базовый класс ошибок API-клиента."""


class ApiClientTimeoutError(ApiClientError):
    """Исключение при таймауте внешнего API."""


class ApiClientNetworkError(ApiClientError):
    """Исключение при сетевых сбоях на транспортном уровне."""


class ApiClientHttpError(ApiClientError):
    """Исключение при HTTP-ответах с кодами 4xx/5xx."""

    def __init__(self, status_code: int, message: str) -> None:
        super().__init__(f"HTTP {status_code}: {message}")
        self.status_code = status_code
        self.message = message
