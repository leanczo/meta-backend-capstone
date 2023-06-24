# Meta Backend Capstone
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

- Get all menus

POST http://localhost:8000/api/menu/

BODY
```json
{
    "title": "Menu 2",
    "price": "123.00",
    "inventory": 3
}
```
RESULT
```json
{
    "id": 2,
    "title": "Menu 2",
    "price": "123.00",
    "inventory": 3
}
```


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
```
user: "super  
password: "123"
```

use http://127.0.0.1:8000/auth/token/logout/ to logout with the token in the header

## Testing
```bash
python manage.py test
```

```sql
GRANT ALL PRIVILEGES ON `test_littlelemon`.* TO 'django'@'localhost';
FLUSH PRIVILEGES;
```

To execute the available unittests, please open the Visual Studio terminal and enter the following command: python manage.py test tests/.
Please ensure that you have activated the virtual environment and navigated into the 'littlelemon' directory prior to running the unit-tests command.

Utilize this path to verify that the web application is serving static HTML content, inclusive of images and styling.
/restaurant

For testing, you can make use of the following API endpoints with Insomnia or Postman clients.
Alternatively, feel free to explore them through your browser of choice.

DJOSER endpoint, for instance, to perform a POST request and register a new user.
/auth/users/

To log in and obtain an authentication token.
/api-token-auth/

To log in using the DJOSER endpoint.
/auth/token/login

Menu items
/api/menu/
/api/menu/{menuItemId}

Table reservations
/api/booking/tables/
/api/booking/tables/{bookingId}