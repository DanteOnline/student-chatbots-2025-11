server:
	python manage.py runserver

lint:
	pylint $(shell git ls-files '*.py')

bot:
	python manage.py run_bot
