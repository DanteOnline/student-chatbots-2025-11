# Homework 7. Bot RAG

Можно задавать вопросы про Гарри Поттера или другим документам :)

## Установка

```commandline
poetry install
```

## Запуск

### QDrant

```commandline
docker compose -f docker-compose.qdrant.yml up
```

### Make

```commandline
make run
```

### Python

```commandline
python main.py
```

## Команды

- /start - главное меню
- /help - главное меню
- /ask <вопрос> - вопрос к боту
