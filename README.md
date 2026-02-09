# Homework 4. Webhook Docker

## Установка

```commandline
poetry install
```

## Запуск

### Make

```commandline
make migrate
```

```commandline
make run
```

```commandline
make ngrok && make run_webhook
```

### Python

```commandline
alembic upgrade head
```

```commandline
python main.py
```

### Docker

```commandline
docker compose up
```

## Команды

- /start - главное меню
- /help - главное меню
- /history - история анкет

## Разделы

- "О нас" - инфо о боте
- "FAQ" - список вопросов
- "Анкета" - заполнение анкеты
