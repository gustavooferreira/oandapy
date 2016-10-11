# vim:ft=make
#
.PHONY: all init test coverage find_todo find_fixme count clean

all: test

init:
	pip install -r requirements.txt

test:
	nosetests

coverage:
	python3 -m nose --with-coverage --cover-erase --cover-package=oandapy tests.test_oanda

find_todo:
	@grep --color=always -PnRe "(#|\"|\').*TODO" oandapy || true

find_fixme:
	@grep --color=always -nRe "#.*FIXME" oandapy || true

count:
	@find . -type f \( -name "*.py" -o -name "*.rst" \) | xargs wc -l

clean:
	rm -f .coverage
	find . -type d -name '__pycache__' | xargs rm -rf
	find . -type f -name '*.pyc' | xargs rm -f
	find . -type d -name '*.ropeproject' | xargs rm -rf

generate_docs:
	@sphinx-apidoc -f -o doc/oandapy oandapy
