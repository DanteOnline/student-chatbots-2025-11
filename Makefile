run:
	python main.py

run_webhook:
	python main_webhook.py

delete_webhook:
	python delete_webhook.py

lint_and_fix:
	poetry run ruff check . --fix

lint_and_fix_unsafe:
	poetry run ruff check . --fix --unsafe-fixes

format:
	poetry run ruff format .

lint:
	poetry run ruff check .

migrate:
	alembic upgrade head

make_migrations:
	alembic revision --autogenerate

ngrok:
	ngrok http 8000