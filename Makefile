install:
	#install commands
format:
	#format code
lint:
	#flake8 or pylint
test:
	#test scripts
deploy:
	#deploy
all: install lint test deploy
