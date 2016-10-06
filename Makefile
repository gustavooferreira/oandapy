# vim:ft=make
#
.PHONY: init test coverage run find_todo find_fixme clean

all: run

init:
	pip install -r requirements.txt

test:
	nosetests
	# python3 -m nose tests.test_oanda

coverage:
	python3 -m nose --with-coverage --cover-erase --cover-package=oanda_api tests.test_oanda

run:
	python3 -m oanda_api.oanda $(env) $(token)

find_todo:
	@grep --color=always -nRe "#.*TODO" oanda_api || true

find_fixme:
	@grep --color=always -nRe "#.*FIXME" oanda_api || true

clean:
	rm -f .coverage
	rm -f tests/*.pyc
	rm -rf tests/__pycache__
	rm -f oanda_api/*.pyc
	rm -rf oanda_api/__pycache__
	rm -f oanda_api/api/*.pyc
	rm -rf oanda_api/api/__pycache__
	rm -f oanda_api/entities/*.pyc
	rm -rf oanda_api/entities/__pycache__
	rm -f oanda_api/enums/*.pyc
	rm -rf oanda_api/enums/__pycache__
	rm -f oanda_api/exceptions/*.pyc
	rm -rf oanda_api/exceptions/__pycache__
