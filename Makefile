.PHONY: all package test test_voter

all: test package

test: test_voter

test_voter:
	python -m unittest test/test_voter.py

package:
	python setup.py sdist

