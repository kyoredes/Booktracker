s:
	poetry run python manage.py runserver
m:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate
sh:
	poetry run python manage.py shell