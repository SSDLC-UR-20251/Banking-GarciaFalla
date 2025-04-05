from _datetime import datetime
import time
from app.validation import *
from app.reading import *
from flask import request, jsonify, redirect, url_for, render_template, session, make_response
from app import app
from app.encryption import hash_with_salt  # Importar la función de hash con sal
from Crypto.Hash import SHA256


@app.route('/api/users', methods=['POST'])
def create_record():
    data = request.form
    email = data.get('email')
    username = data.get('username')
    nombre = data.get('nombre')
    apellido = data.get('Apellidos')
    password = data.get('password')
    dni = data.get('dni')
    dob = data.get('dob')
    errores = []
    print(data)
    # Validaciones
    if not validate_email(email):
        errores.append("Email inválido")
    if not validate_pswd(password):
        errores.append("Contraseña inválida")
    if not validate_dob(dob):
        errores.append("Fecha de nacimiento inválida")
    if not validate_dni(dni):
        errores.append("DNI inválido")
    if not validate_user(username):
        errores.append("Usuario inválido")
    if not validate_name(nombre):
        errores.append("Nombre inválido")
    if not validate_name(apellido):
        errores.append("Apellido inválido")

    if errores:
        return render_template('form.html', error=errores)

    email = normalize_input(email)

    # Generar hash y sal para la contraseña
    hash_result, salt = hash_with_salt(password)

    db = read_db("db.txt")
    db[email] = {
        'nombre': normalize_input(nombre),
        'apellido': normalize_input(apellido),
        'username': normalize_input(username),
        'password': hash_result,  # Almacenar el hash
        'salt': salt,  # Almacenar la sal
        "dni": dni,
        'dob': normalize_input(dob),
    }

    write_db("db.txt", db)
    return redirect("/login")


# Endpoint para el login
@app.route('/api/login', methods=['POST'])
def api_login():
    email = normalize_input(request.form['email'])
    password = normalize_input(request.form['password'])

    db = read_db("db.txt")
    if email not in db:
        error = "Credenciales inválidas"
        return render_template('login.html', error=error)

    user_data = db.get(email)
    stored_hash = user_data["password"]
    salt = user_data["salt"]

    # Generar hash de la contraseña proporcionada con la sal almacenada
    h = SHA256.new()
    h.update(bytes.fromhex(salt) + password.encode('utf-8'))
    provided_hash = h.hexdigest()

    # Comparar el hash proporcionado con el hash almacenado
    if provided_hash == stored_hash:
        return redirect(url_for('customer_menu'))
    else:
        error = "Credenciales inválidas"
        return render_template('login.html', error=error)

# Página principal del menú del cliente
@app.route('/customer_menu')
def customer_menu():
    db = read_db("db.txt")

    transactions = read_db("transaction.txt")
    current_balance = 100
    last_transactions = []
    message = request.args.get('message', '')
    error = request.args.get('error', 'false').lower() == 'true'
    return render_template('customer_menu.html',
                           message=message,
                           nombre="",
                           balance=current_balance,
                           last_transactions=last_transactions,
                           error=error,)

# Endpoint para leer un registro
@app.route('/records', methods=['GET'])
def read_record():
    db = read_db("db.txt")
    return render_template('records.html', users=db)
