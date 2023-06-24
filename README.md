# meta-backend-capstone
This is a capstone project for the Meta Back-End Development course

### Commands

``` bash
python -m venv capstone
capstone\Scripts\activate
pip install django

-- create a django project
django-admin startproject littlelemon
-- run development server
cd littlelemon
python manage.py runserver
-- create a django app 
python manage.py startapp restaurant

pip3 install mysqlclient

create database littlelemon;
use littlelemon;

CREATE USER 'django'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON littlelemon.* TO 'django'@'localhost';
python3 manage.py migrate 
python3 manage.py makemigrations

python manage.py createsuperuser
user:super
email: super@gmail.com
password: 123


```


