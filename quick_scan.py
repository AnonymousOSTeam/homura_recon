import socket

def get_service_name(port):
    try:
        return socket.getservbyport(port)
    except:
        return "Unknown Service"

def run(target):
    print(f"\n--- [HOMURA_RECON] Advanced Port Analysis ---")
    # We'll use the main scanner logic here
    from homura_recon import HomuraRecon
    
    scanner = HomuraRecon(target)
    # Scan common ports for a quicker defensive check
    common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3306, 3389, 8080]
    
    print(f"[*] Performing rapid scan on common ports for {target}...")
    
    # Manual scan for common ports
    open_ports = []
    for port in common_ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            if s.connect_ex((target, port)) == 0:
                open_ports.append(port)
    
    if not open_ports:
        print("[+] No common open ports found.")
    else:
        for port in open_ports:
            service = get_service_name(port)
            print(f"[!] Port {port} is OPEN - Service: {service}")
