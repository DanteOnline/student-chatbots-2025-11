run:
	python .\main.py

lint:
	poetry run pylint $(shell git ls-files '*.py')