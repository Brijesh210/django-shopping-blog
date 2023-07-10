release: python manage.py migrate
web: gunicorn shopping.wsgi --workers 2 --log-file -