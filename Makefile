test:
	py.test -rs tests/

clean-pyc:
	find . -name "*.pyc" -exec rm {} +
	find . -name "__pycache__" -exec rm -r {} +

pep8:
	pep8 practices/ tests/
