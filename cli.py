import argparse
import sys
from homura_recon import HomuraRecon

def main():
    parser = argparse.ArgumentParser(description="Homura_Recon - Defensive Port Scanner Alternative to Nmap")
    parser.add_argument("target", help="Target IP address to scan")
    parser.add_argument("-p", "--ports", help="Port range (e.g., 1-1000)", default="1-1024")
    parser.add_argument("-t", "--threads", type=int, help="Number of threads (default: 100)", default=100)
    
    args = parser.parse_args()
    
    try:
        port_start, port_end = map(int, args.ports.split('-'))
    except ValueError:
        print("Error: Ports must be in format start-end (e.g. 1-1024)")
        sys.exit(1)
    
    recon = HomuraRecon(args.target, threads=args.threads)
    recon.run(port_range=(port_start, port_end))

if __name__ == "__main__":
    main()
