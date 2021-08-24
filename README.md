# Sportskeeda
To start the django development environment please install the requirements.txt
After configuring all the requirements do the below steps to execute the api.
1. python manage.py runserver
2. To get the response for a particular string provide the below link.
http://127.0.0.1:8000/api/spreedsheet/<string>

Example: http://127.0.0.1:8000/api/spreedsheet/BBB

GET /api/spreedsheet/BBB
HTTP 200 OK
Allow: OPTIONS, GET
Content-Type: application/json
Vary: Accept

{
    "BBB": 1406
