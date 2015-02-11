web: gunicorn AP_Agenda.wsgi --log-file -
web: python manage.py collectstatic --noinput; gunicorn AP_Agenda.wsgi
