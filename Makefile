dev:
	uv run python manage.py runserver
migrate:
	uv run python manage.py makemigrations
	uv run python manage.py migrate
sh:
	uv run python manage.py shell
test:
	uv run pytest -vvvvv -s
test-authors:
	uv run pytest -vvvvv -s authors
test-booklists:
	uv run pytest -vvvvv -s booklists
test-books:
	uv run pytest -vvvvv -s books
test-users:
	uv run pytest -vvvvv -s users
urls:
	uv run python manage.py show_urls
cache:
	uv run python manage.py clear_cache
docker:
	docker build -t booktracker .
	docker run -it -d -p 8000:8000  --name booktracker booktracker
	docker exec -it booktracker /bin/bash
indx:
	uv run python manage.py search_index --rebuild
lint:
	uv run flake8