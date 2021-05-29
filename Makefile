install:
	pip install -r requirements.txt
 
setup:
	python3 -m venv ~/.finalproject434
 
test:
	python -m pytest -vv --cov=finalproject434lib tests/*.py
 
lint:
	pylint --disable=R,C linttest.py
   #syntax checks
 
all:
	install lint test