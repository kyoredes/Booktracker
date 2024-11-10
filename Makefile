s:
	poetry run python manage.py runserver
m:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate
sh:
	poetry run python manage.py shell
test:
	poetry run pytest -vvvvv -s
urls:
	poetry run python manage.py show_urls
cache:
	poetry run python manage.py clear_cache