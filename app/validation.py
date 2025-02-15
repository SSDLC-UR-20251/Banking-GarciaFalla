from datetime import datetime
import re

import unicodedata

def normalize_input(data):
    return unicodedata.normalize("NFKC", data).strip()


# Validar el email   3️⃣ Validación de Correo Electrónico
def validate_email(email):
    email = normalize_input(email)
    return bool(re.fullmatch(r"^[a-zA-Z0-9._%+-]+@urosario\.edu\.co$", email))

# Validar la edad (mínimo 16 años)   4️⃣ Validación de Fecha de Nacimiento
def validate_dob(dob):
    try:
        birth_date = datetime.strptime(dob, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return  100 >= age >= 16
    except ValueError:
        return False

# Validar el nombre de usuario (solo letras y puntos)   1️⃣ Validación de Usuario
def validate_user(user):
    user = normalize_input(user)
    return bool(re.fullmatch(r"^[a-zA-Z]+.[a-zA-Z]+$", user))

# Validar el documento de identificación (numérico, 10 dígitos, empieza con 1000000000)  5️⃣ Validación de Documento de Identificación
def validate_dni(dni):
    return bool(re.fullmatch(r"^1\d{9}$", dni))


# Validar la contraseña  2️⃣ Validación de Contraseña
def validate_pswd(pswd):
    pswd = normalize_input(pswd)
    if not (8 <= len(pswd) <= 35):
        return False
    if not re.search(r"[a-z]", pswd):
        return False
    if not re.search(r"[A-Z]", pswd):
        return False
    if not re.search(r"\d", pswd):
        return False
    if not re.search(r"[#*@$%&\-!+=?]", pswd):
        return False
    return True

# Validar el nombre (permitir solo letras y espacios)
def validate_name(name):
    name = normalize_input(name)
    return bool(re.fullmatch(r"^[a-zA-Z ]+$", name))
