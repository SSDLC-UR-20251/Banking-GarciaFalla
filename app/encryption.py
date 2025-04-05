from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256

def encrypt_aes(texto, clave):
    # Convertir el texto a bytes
    texto_bytes = texto.encode()

    # Crear un objeto AES con la clave proporcionada
    cipher = AES.new(clave, AES.MODE_EAX)

    # Cifrar el texto
    nonce = cipher.nonce
    texto_cifrado, tag = cipher.encrypt_and_digest(texto_bytes)

    # Convertir el texto cifrado en bytes a una cadena de texto
    texto_cifrado_str = texto_cifrado.hex()

    # Devolver el texto cifrado, el nonce y el tag
    return texto_cifrado_str, nonce.hex(), tag.hex()

def decrypt_aes(texto_cifrado_str, nonce_str, tag_str, clave):
    # Convertir el texto cifrado, nonce y tag de cadena de texto a bytes
    texto_cifrado = bytes.fromhex(texto_cifrado_str)
    nonce = bytes.fromhex(nonce_str)
    tag = bytes.fromhex(tag_str)

    # Crear un objeto AES con la clave y el nonce proporcionados
    cipher = AES.new(clave, AES.MODE_EAX, nonce=nonce)

    # Descifrar el texto
    texto_descifrado = cipher.decrypt_and_verify(texto_cifrado, tag)

    # Convertir los bytes del texto descifrado a una cadena de texto
    return texto_descifrado.decode()

def hash_with_salt(texto):
    # Generar una sal aleatoria
    salt = get_random_bytes(16)  # Sal de 16 bytes

    # Convertir el texto en claro a bytes
    texto_bytes = texto.encode('utf-8')

    # Crear un objeto de hash SHA-256
    h = SHA256.new()

    # Agregar la sal y el texto plano al hash
    h.update(salt + texto_bytes)

    # Calcular el hash final
    hash_result = h.hexdigest()

    # Devolver el hash y la sal
    return hash_result, salt.hex()

if __name__ == '__main__':
    # Ejemplo de uso para AES
    texto = "Hola Mundo"
    clave = get_random_bytes(16)  # Clave de 16 bytes para AES-128
    texto_cifrado, nonce, tag = encrypt_aes(texto, clave)
    print("Texto cifrado:", texto_cifrado)
    print("Nonce:", nonce)
    print("Tag:", tag)

    texto_descifrado = decrypt_aes(texto_cifrado, nonce, tag, clave)
    print("Texto descifrado:", texto_descifrado)

    # Ejemplo de uso para hash con sal
    texto_original = "Este es un mensaje secreto"
    hash_result, salt = hash_with_salt(texto_original)
    print("Texto original:", texto_original)
    print("Salt:", salt)
    print("Hash resultante:", hash_result)
