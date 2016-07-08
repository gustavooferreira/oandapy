# vim:ft=make
#
.PHONY: init test coverage run clean

all: run

init:
	pip install -r requirements.txt

test:
	python3 -m nose tests.test_oanda

coverage:
	python3 -m nose --with-coverage --cover-package=oanda_api tests.test_oanda

run:
	python3 -m oanda_api.oanda $(env) $(token)

clean:
	rm -f .coverage
	rm -f tests/*.pyc
	rm -rf tests/__pycache__
	rm -f oanda_api/*.pyc
	rm -rf oanda_api/__pycache__
