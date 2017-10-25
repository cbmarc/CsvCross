init:
    pip install -r requirements.txt

test:
    python -m unittest

coverage:
	python -m coverage run -m unittest

.PHONY: init test coverage