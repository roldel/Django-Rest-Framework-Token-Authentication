# Django Rest Framework Token-Authentication
This project demonstrates how to implement Django REST Framework's built-in token authentication system for secure API client authentication. Users can obtain, store, and use tokens to authenticate API requests.


Commands list:

docker compose build
docker compose run run web django-admin startproject core .
docker compose up

docker exec -it {container_id} sh
python manage.py startapp api_auth
python manage.py migrate
python manage.py createsuperuser
