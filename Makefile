.PHONY: up
up:
	docker compose up -d

.PHONY: down
down:
	docker compose down

.PHONY: stop
stop:
	docker compose stop

.PHONY: build
build:
	docker compose up --build -d
