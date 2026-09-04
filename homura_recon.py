import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

class HomuraRecon:
    def __init__(self, target, threads=100):
        self.target = target
        self.threads = threads
        self.open_ports = []

    def scan_port(self, port):
        """Attempts to connect to a specific port to check if it is open."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1) 
                result = s.connect_ex((self.target, port))
                if result == 0:
                    return port
        except Exception:
            pass
        return None

    def run(self, port_range=(1, 1024)):
        """Orchestrates the scan using a thread pool for speed."""
        print(f"\n[*] Homura_Recon initializing scan on: {self.target}")
        print(f"[*] Port Range: {port_range[0]} - {port_range[1]}")
        print(f"[*] Threads: {self.threads}")
        print("-" * 50)
        
        start_time = time.time()
        
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = {executor.submit(self.scan_port, port): port for port in range(port_range[0], port_range[1] + 1)}
            
            for future in as_completed(futures):
                port = future.result()
                if port:
                    self.open_ports.append(port)
                    try:
                        service = socket.getservbyport(port)
                    except:
                        service = "Unknown"
                    print(f"[!] Port {port} is OPEN | Service: {service}")

        end_time = time.time()
        duration = end_time - start_time
        
        print("-" * 50)
        print(f"[*] Scan completed in {duration:.2f} seconds.")
        print(f"[*] Total Open Ports: {len(self.open_ports)}")
        return sorted(self.open_ports)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        target = sys.argv[1]
        recon = HomuraRecon(target)
        recon.run()
    else:
        print("Usage: python3 homura_recon.py <target>")
