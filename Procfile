release: sh -c 'python manage.py makemigrations && python manage.py migrate && python manage.py loaddata initial_watchlist_data.json'
web: python manage.py migrate && gunicorn project_django.wsgi --log-file -
