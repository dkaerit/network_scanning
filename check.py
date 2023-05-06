import re

ip_checks = {
    "format_ip": (lambda ip: (re.match(r"(\d{1,3}\.){3}\d{1,3}(\/\d{1,2})?$", ip)), 
        ValueError("Dirección IP inválida.")),
    "valid_ip_values": (lambda ip: all(int(value) <= 254 for value in ip.split('.')[:-1]) and 0 <= int(ip.split('.')[-1].split('/')[0]) <= 254, 
        ValueError("Los valores de la dirección IP no pueden ser mayores a 254."))
}

port_checks = {
    "valid_port_single": (lambda port: (0 <= int(port) <= 65535), 
        ValueError("El puerto debe estar entre 0 y 65535.")),
}

range_port_checks = {
    "valid_ports_range": (lambda initial, final: (initial <= final), 
        ValueError("El puerto inicial debe ser menor o igual que el puerto final.")),
}

def run_checks(checks, *values):
    for name, (condition, exception) in checks.items():
        if not condition(*values): raise exception
