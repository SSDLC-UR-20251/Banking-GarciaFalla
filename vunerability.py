# EJEMPLO 1
urlpatterns = [
    # Route to code_execution
    url(r'^code-ex1$', code_execution_bad, name='code-execution-bad'),
    url(r'^code-ex2$', code_execution_good, name='code-execution-good')
]

def code_execution(request):
    if request.method == 'POST':
        first_name = base64.decodestring(request.POST.get('first_name', ''))
        #BAD -- Allow user to define code to be run.
        exec("setname('%s')" % first_name)

def code_execution(request):
    if request.method == 'POST':
        first_name = base64.decodestring(request.POST.get('first_name', ''))
        #GOOD --Call code directly
        setname(first_name)

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
