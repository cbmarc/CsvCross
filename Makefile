init:
    pip install -r requirements.txt

test:
    python -m unittest

coverage:
	python -m coverage run -m unittest

clean:
    find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

.PHONY: init test coverage clean