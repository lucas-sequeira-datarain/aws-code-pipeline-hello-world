.PHONY: help lint

.DEFAULT: help

help:
	@echo "make lint"
	@echo "       run lint"

lint:
	flake8 --ignore E305,E501,W503 --exclude .git,__pycache
	bandif -r -lll .