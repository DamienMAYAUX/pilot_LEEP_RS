web: gunicorn oTree.manage:app --log-file – --log-level debug
python manage.py collectstatic --noinput
manage.py migrate