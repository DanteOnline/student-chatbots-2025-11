run:
	python .\main.py

lint:
	pylint $(shell git ls-files '*.py')