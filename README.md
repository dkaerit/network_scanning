# Herramientas de escaneo de redes en Python
Este repositorio contiene una colección de herramientas de escaneo de redes escritas en Python para ayudar en el descubrimiento y análisis de hosts en una red.

## Funcionalidades
Este repositorio incluye las siguientes herramientas:

Ping_sweep: para detectar hosts activos en una subred determinada.
Port_scanning: para identificar los puertos abiertos en un host.
Fingerprinting: para identificar el sistema operativo y la versión de software en ejecución en un host.
Estas herramientas se pueden utilizar para detectar posibles vulnerabilidades y fortalecer la seguridad de una red.

## Requisitos
Para utilizar estas herramientas es necesario tener instalado Python 3 y los siguientes paquetes:

requests
colorama

## Uso
Para ejecutar las herramientas, simplemente debes abrir la terminal y ejecutar el archivo correspondiente. Por ejemplo, para realizar un escaneo de puertos en un host:


```bash
$ python3 main.py
$ python3 fingerprinting.py
```

También es posible modificar los puertos a escanear y el rango de direcciones IP en los archivos correspondientes.

## Contribuir
Si deseas contribuir a este proyecto, puedes hacerlo a través de pull requests. Siéntete libre de reportar problemas o sugerencias en la sección de issues.
