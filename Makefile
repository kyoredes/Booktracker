s:
	poetry run python manage.py runserver
m:
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
urls:
	poetry run python manage.py show_urls
cache:
	poetry run python manage.py clear_cache