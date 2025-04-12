# EJEMPLO 1
def code_execution(request):
    if request.method == 'POST':
        first_name = base64.decodestring(request.POST.get('first_name', ''))
        #BAD -- Allow user to define code to be run.
        exec("setname('%s')" % first_name)

# EJEMPLO 2 

def show_user(request, username):
    with connection.cursor() as cursor:
        # BAD -- Using string formatting
        cursor.execute("SELECT * FROM users WHERE username = '%s'" % username)
        user = cursor.fetchone()
 
        # BAD -- Manually quoting placeholder (%s)
        cursor.execute("SELECT * FROM users WHERE username = '%s'", username)
        user = cursor.fetchone()
 
