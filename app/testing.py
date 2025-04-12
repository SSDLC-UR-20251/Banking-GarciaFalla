import requests

# URL de la API
url = "http://127.0.0.1:5000/api/users"

# Datos de prueba para el usuario
payload = {
    "username": "b.b",
 
    "dob": "2005-06-15",
    "dni": "1000000001",
    "nombre": "aaaa",
    "Apellidos": "bbb"
}

# Cabeceras opcionales
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Enviar solicitud POST
response = requests.post(url, data=payload, headers=headers)

# Mostrar respuesta del servidor
print("Código de estado:", response.status_code)
try:
    print("Respuesta JSON:", response.json())
except requests.exceptions.JSONDecodeError:
    print("Respuesta no es JSON. Respuesta cruda:", response.text)