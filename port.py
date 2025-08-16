import socket

def scan_ports(target, ports):
    print(f"Scanning {target} for open ports...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout for slow hosts
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        sock.close()
