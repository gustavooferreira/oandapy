# vim:ft=make
#
.PHONY: init test coverage run find_todo find_fixme proxy_testing count clean

all: run

init:
	pip install -r requirements.txt

test:
	nosetests
	# python3 -m nose tests.test_oanda

coverage:
	python3 -m nose --with-coverage --cover-erase --cover-package=oandapy tests.test_oanda

run:
	python3 -m oandapy.oanda $(env) $(token)

find_todo:
	@grep --color=always -PnRe "(#|\"|\').*TODO" oandapy || true

find_fixme:
	@grep --color=always -nRe "#.*FIXME" oandapy || true

proxy_testing:
	set -e; \
	export HTTP_PROXY="http://127.0.0.1:8080"; \
	export HTTPS_PROXY="http://127.0.0.1:8080"; \
	ipython

count:
	@find . -name '*.py' | xargs wc -l

clean:
	rm -f .coverage
	rm -f tests/*.pyc
	rm -rf tests/__pycache__
	rm -f oandapy/*.pyc
	rm -rf oandapy/__pycache__
	rm -f oandapy/api/*.pyc
	rm -rf oandapy/api/__pycache__
	rm -f oandapy/entities/*.pyc
	rm -rf oandapy/entities/__pycache__
	rm -f oandapy/containers/*.pyc
	rm -rf oandapy/containers/__pycache__
	rm -f oandapy/enums/*.pyc
	rm -rf oandapy/enums/__pycache__
	rm -f oandapy/exceptions/*.pyc
	rm -rf oandapy/exceptions/__pycache__
