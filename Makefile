run:
	python main.py

run_webhook:
	python main_webhook.py

delete_webhook:
	python delete_webhook.py

lint:
	ruff check .

lint_and_fix:
	ruff check . --fix

format:
	ruff format .

ngrok:
	ngrok http 8000