# EJEMPLO 1
from django.conf.urls import url
from django.db import connection


def show_user(request, username):
    with connection.cursor() as cursor:

        # GOOD -- Using parameters
        cursor.execute("SELECT * FROM users WHERE username = %s", username)
        user = cursor.fetchone()


urlpatterns = [url(r'^users/(?P<username>[^/]+)$', show_user)]

# EJEMPLO 2 
from argon2 import PasswordHasher

def get_initial_hash(password: str):
    ph = PasswordHasher()
    return ph.hash(password) # GOOD

def check_password(password: str, known_hash):
    ph = PasswordHasher()
    return ph.verify(known_hash, password) # GOOD

AWS_SECRET_KEY = 'AKIAIOSFODNN7EXPAMPLE'

PASSWORD = "ASKDJASLKDJASD123456"
