import socket

def scan_ports(target, ports):
    print(f"Scanning {target} for open ports...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout for slow hosts
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        sock.close()

# Example usage
target_ip = input("Enter target IP (e.g. 192.168.1.1): ")
ports_to_scan = range(1, 1025)  # Common ports (1-1024)
scan_ports(target_ip, ports_to_scan) 