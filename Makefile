# Makefile for football_tournament-technical_test

.PHONY: up down build migrate makemigrations test seed shell

up:
	docker compose up -d --build

down:
	docker compose down

build:
	docker compose build

migrate:
	docker compose exec web python manage.py migrate

makemigrations:
	docker compose exec web python manage.py makemigrations

test:
	docker compose exec web python manage.py test

seed:
	docker compose exec web python manage.py seed_equipes
	docker compose exec web python manage.py seed_joueurs

shell:
	docker compose exec web python manage.py shell
