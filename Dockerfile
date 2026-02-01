FROM python:3.13-slim

# Устанавливаем poetry
RUN pip install --upgrade pip
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry install
COPY ./ ./

CMD ["poetry", "run", "python", "main_webhook.py"]