import os
import sys
import threading

# Add the current directory to the sys.path to find modules in the same directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from cli import get_bindable_ips, choose_ip
from filetraffic.ftp import start_ftp_server
from filetraffic.tftp import start_tftp_server
from http_server import start_http_server

def launch_server(server_name, target, ip):
    print(f"[+] Starting {server_name} server on {ip}...")
    thread = threading.Thread(target=target, args=(ip,), daemon=True)
    thread.start()

def fileriver():
    ips = get_bindable_ips()
    if not ips:
        print("No available IPs found for binding.")
        sys.exit(1)

    selected_ip = choose_ip(ips)
    launch_server("FTP", start_ftp_server, selected_ip)
    launch_server("TFTP", start_tftp_server, selected_ip)
    launch_server("HTTP", start_http_server, selected_ip)

    print("[✔] All selected servers are running. Press Ctrl+C to stop.")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\n[!] Servers stopped.")

if __name__ == '__main__':
    fileriver()
