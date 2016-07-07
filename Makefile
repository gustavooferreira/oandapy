# vim:ft=make

all:
	@echo "TODO: In progress"

init:
	pip install -r requirements.txt

test:
	python -m unittest tests/test_oanda.py
