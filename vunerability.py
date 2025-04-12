# EJEMPLO 1
@app.route("/example_bad")
def example_bad():
    rfs_header = request.args["rfs_header"]
    response = Response()
    custom_header = "X-MyHeader-" + rfs_header
    # BAD: User input is used as part of the header name.
    response.headers[custom_header] = "HeaderValue" 
    return response

@app.route("/example_good")
def example_bad():
    rfs_header = request.args["rfs_header"]
    response = Response()
    custom_header = "X-MyHeader-" + rfs_header.replace("\n", "").replace("\r","").replace(":","")
    # GOOD: Line break characters are removed from the input.
    response.headers[custom_header] = "HeaderValue" 
    return response

# EJEMPLO 2 

from django.conf.urls import url
from django.db import connection


def show_user(request, username):
    with connection.cursor() as cursor:
        # BAD -- Using string formatting
        cursor.execute("SELECT * FROM users WHERE username = '%s'" % username)
        user = cursor.fetchone()

        # GOOD -- Using parameters
        cursor.execute("SELECT * FROM users WHERE username = %s", username)
        user = cursor.fetchone()

        # BAD -- Manually quoting placeholder (%s)
        cursor.execute("SELECT * FROM users WHERE username = '%s'", username)
        user = cursor.fetchone()

urlpatterns = [url(r'^users/(?P<username>[^/]+)$', show_user)]
