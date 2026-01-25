run:
	python .\main.py

lint_and_fix:
	poetry run ruff check . --fix

format:
	poetry run ruff format .

lint:
	poetry run ruff check .