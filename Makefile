.PHONY: install

isort:
	  isort .

test:
	  python3 pytest

flake8:
	  python3 -m flake8 .

clean-build:
	  rm -rf *.egg-info dist build

clean-pyc:
	  find . -name '*.pyc' -delete
	  find . -name '*.pyo' -delete

trim:
	  trim .

unify:
	  unify -i -r .

trail-comma:
	  find . -name '*.py' -exec add-trailing-comma {} +
