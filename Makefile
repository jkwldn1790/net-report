help:
	@echo
	@echo -- Available Commands --
	@echo
	@echo build: Build docker container for nettest
	@echo run: Run nettest
	@echo

build:
	docker build -t nettest:v1 .

run:
	docker run -it --network host nettest:v1

setup:
	docker-compose up -d
	./nettest/create_table.py