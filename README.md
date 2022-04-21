# Django-REST-framework-example-app
with Redis and Celery

Setting up a new environment 
```
python3 -m venv venv
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
celery --app=drf_example_app worker -l info
```
