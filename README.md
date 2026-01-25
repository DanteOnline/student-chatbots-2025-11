# Homework 3. Bot with Database

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

### Python

```commandline
alembic upgrade head
```

```commandline
python main.py
```

## Команды

- /start - главное меню
- /help - главное меню
- /history - история анкет

## Разделы

- "О нас" - инфо о боте
- "FAQ" - список вопросов
- "Анкета" - заполнение анкеты
