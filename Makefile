# vim:ft=make
#
.PHONY: all init test coverage find_todo find_fixme count clean generate_docs

all: test

init:
	pip install -r requirements.txt

test:
	nosetests

coverage:
	# @python3 -m nose --with-coverage --cover-erase --cover-package=oandapy tests.test_oanda || true
	coverage run --source=oandapy make test

find_todo:
	@grep --color=always -PnRe "(#|\"|\').*TODO" oandapy || true

find_fixme:
	@grep --color=always -nRe "#.*FIXME" oandapy || true

count:
	@find . -type f \( -name "*.py" -o -name "*.rst" \) | xargs wc -l

clean:
	rm -f .coverage
	rm -rf oandapy.egg-info
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' | xargs rm -rf
	find . -type d -name '*.ropeproject' | xargs rm -rf

generate_docs:
	@sphinx-apidoc -f -o doc/oandapy oandapy
