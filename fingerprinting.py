#! /usr/bin/python3
import requests
from colorama import Fore, Style

# obtenemos la respuesta de los servicios
def fingerprint(host:str, header):
    respuesta = requests.get(f"http://{host}", headers = header) # Obtenemos la respuesta del servidor
    codigo_estado = respuesta.status_code # 200, 301, 302 ...
    cabeceras = respuesta.headers # cabecera de la petición

    print(f"STATUS: {codigo_estado}\n")
    for (key,value) in cabeceras.items():
        print(f"{key}: {value}")

#fingerprint("www.python.org")
#fingerprint('www.httpbin.org')
#fingerprint('192.168.10.4:80')
fingerprint('www.paginasamarillas.es/', {"User-agent": "Sasuki"})
