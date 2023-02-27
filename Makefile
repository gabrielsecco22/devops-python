install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format code - All .py files in all folders and subfolders
	black ./**/*.py
lint:
	#flake8 or pylint
test:
	#test scripts
deploy:
	#deploy
all: install lint test deploy
