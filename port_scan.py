#! /usr/bin/python3
import socket
from colorama import Fore, Style
import check
import random


def port_scan(IP_ADDRESS:str, FIRST_PORT:int = 0, FINAL_PORT:int = 1023):    
    try:
        check.run_checks(check.port_checks, FIRST_PORT)
        check.run_checks(check.port_checks, FINAL_PORT)
        check.run_checks(check.range_port_checks, FIRST_PORT, FINAL_PORT)
    except ValueError as e: print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

    ports = list(range(FIRST_PORT, FINAL_PORT+1))
    random.shuffle(ports)

    for port in ports:
        print(f"\rEcaneando {f'{IP_ADDRESS}:{port}'.ljust(18)}", end="")
        # shuffle ports
        # random timeout
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creamos un socket IPv4 de tipo TCP
        soc.settimeout(0.05) # Establecemos un tiempo de espera máximo de 100 ms
        respuesta = soc.connect_ex((str(IP_ADDRESS),port)) # Tratamos de establecer la conexión
        soc.close() # Cerramos el socket
        
        if respuesta == 0: 
            print(f"{Fore.CYAN} ———> Puerto abierto{Style.RESET_ALL}")
