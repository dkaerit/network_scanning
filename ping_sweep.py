#! /usr/bin/python3
import os
import ipaddress
from colorama import Fore, Style
import check
import port_scan as ps

def ping_sweep():
    #IP_ADDRESS = str(input("IP/MASC: "))
    #FIRST_PORT = int(input("Puerto de inicio (0-65535): "))
    #FINAL_PORT = int(input("Puerto final (0-65535): "))

    IP_ADDRESS = "192.168.10.0/28" # En formato CIDR
    ips = ipaddress.IPv4Network(IP_ADDRESS).hosts()

    try:
        check.run_checks(check.ip_checks, IP_ADDRESS)
    except ValueError as e: print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

    for ip in ips:
        print("\rpinging {:<15}".format(str(ip)), end="")
        comando = f"ping -c 1 -W 0.05 {ip} > /dev/null"
        resultado = os.system(comando)
        if resultado == 0: 
            print(f"{Fore.CYAN} ———> Se encontró{Style.RESET_ALL}")
            ps.port_scan(str(ip))
