# blog-app
sample blog app

to install:

virtualenv -p python3 env

. env/bin/activate

pip3 install -r requirements-txt 

to run

django-admin startproject blogapp .

cd blogapp/

django-admin startapp app

python manage.py migrate

python manage.py makemigrations app

python manage.py migrate

python manage.py runserver
