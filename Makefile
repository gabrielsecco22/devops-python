install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format code - All .py files in all folders and subfolders
	black ./**/*.py *.py
lint:
	#flake8 or pylint
	pylint --disable=R,C ./**/*.py *.py
test:
	#test scripts
	python -m pytest -vv --cov=main
build: 
	#build container
deploy:
	#deploy
all: install lint test deploy
