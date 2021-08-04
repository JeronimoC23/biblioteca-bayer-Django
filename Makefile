migrate-project:
	docker-compose run --no-deps web python3 manage.py migrate

run-project:
	docker-compose up 