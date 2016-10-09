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
	@find . -type f \( -name "*.py" -o -name "*.rst" \) | xargs wc -l

clean:
	rm -f .coverage
	find . -type d -name '__pycache__' | xargs rm -rf
	find . -type f -name '*.pyc' | xargs rm -f
	find . -type d -name '*.ropeproject' | xargs rm -rf
