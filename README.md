# meta-backend-capstone
This is a capstone project for the Meta Back-End Development course

# Commands

``` bash
python -m venv capstone
capstone\Scripts\activate
pip install django
# create a django project
django-admin startproject littlelemon
# run development server
cd littlelemon
python manage.py runserver
# create a django app 
python manage.py startapp restaurant
# install client
pip3 install mysqlclient
```

```sql
create database littlelemon;
use littlelemon;
CREATE USER 'django'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON littlelemon.* TO 'django'@'localhost';
```

```bash
python3 manage.py migrate 
python3 manage.py makemigrations
python manage.py createsuperuser
#user:super
#email: super@gmail.com
#password: 123
pip3 install djangorestframework
```

GET in 
http://localhost:8000/api/menu/1

```json
{
    "id": 1,
    "title": "Menu 1",
    "price": "123.00",
    "inventory": 4
}
```
GET in 
http://localhost:8000/api/menu

- Add all menus

GET in 
http://localhost:8000/api/booking/tables

```json
[
    {
        "id": 1,
        "name": "Booking 1",
        "number_of_guests": 6,
        "booking_date": "2023-06-06T17:41:53Z"
    }
]
```
POST http://localhost:8000/api/api-token-auth/
```json
{
    "token": "a9d223579062329a541eb8eb8206c52c8b15c974"
}
```

Add authorization to the endpoints, so you have to send a header in the request with the Authorization title: Token [VALUE]

```bash
pip install djoser
```

navigate to http://127.0.0.1:8000/auth/token/login/ to get the token
user: "super"
password: "123"