# Makefile
.PHONY: start stop install test

install:
	chmod +x setup.sh && ./setup.sh

start:
	docker-compose up -d --build

stop:
	docker-compose down

test:
	pytest -q
