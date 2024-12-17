dev:
	poetry run python manage.py runserver
migrate:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate
sh:
	poetry run python manage.py shell
test:
	poetry run pytest -vvvvv -s
test-authors:
	poetry run pytest -vvvvv -s authors
test-booklists:
	poetry run pytest -vvvvv -s booklists
test-books:
	poetry run pytest -vvvvv -s books
test-users:
	poetry run pytest -vvvvv -s users
urls:
	poetry run python manage.py show_urls
cache:
	poetry run python manage.py clear_cache
docker:
	docker build -t booktracker .
	docker run -it -d -p 8000:8000  --name booktracker booktracker
	docker exec -it booktracker /bin/bash
indx:
	poetry run python manage.py search_index --rebuild
lint:
	poetry run flake8