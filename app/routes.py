from flask import render_template, redirect, url_for, session, request
from app import app
from app.encryption import decrypt_aes, ofuscar_dni
from app.reading import read_db


# app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/deposit', methods=['GET'])
def deposit():
    
    if 'email' not in session:
        # Redirigir a la página de inicio de sesión si el usuario no está autenticado
        error_msg = "Por favor, inicia sesión para acceder a esta página."
        return render_template('login.html', error=error_msg)
    cookie = request.cookies.get('darkmode')
    return render_template('deposit.html',darkmode = cookie)


@app.route('/register', methods=["GET", "POST"])
def register():
    return render_template('form.html')


@app.route('/login', methods=["GET"])
def login():
    return render_template("login.html")


@app.route('/edit_user/<email>', methods=['GET'])
def edit_user(email):
    if 'email' not in session:
        # Redirigir a la página de inicio de sesión si el usuario no está autenticado
        error_msg = "Por favor, inicia sesión para acceder a esta página."
        return render_template('login.html', error=error_msg)
    db = read_db("db.txt")
    
    cookie = request.cookies.get('darkmode')
    if email not in db:
        return redirect(url_for('records', message="Usuario no encontrado"),darkmode = cookie)

    user_info = db[email]

    return render_template('edit_user.html', user_data=user_info, email=email,darkmode = cookie)


# Formulario de retiro
@app.route('/withdraw', methods=['GET'])
def withdraw():
    if 'email' not in session:
        return redirect(url_for('login', message="Por favor, inicia sesión."))
    email = session.get('email')
    print(email)
    transactions = read_db("transaction.txt")
    current_balance = sum(float(t['balance']) for t in transactions.get(email, []))
    cookie = request.cookies.get('darkmode')
    return render_template('withdraw.html', balance=current_balance,darkmode = cookie)
