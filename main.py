import socket
import netifaces
import sys
import threading

from filetraffic import ftp, tftp
import http_server 

def get_bindable_ips():
    candidates = []
    for iface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(iface)
        if netifaces.AF_INET in addrs:
            for addr in addrs[netifaces.AF_INET]:
                ip = addr.get('addr')
                if ip and not ip.startswith('169.254') and not ip.startswith('127.'):
                    if is_bindable(ip):
                        candidates.append((iface, ip))
    return candidates

def is_bindable(ip, port=0):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((ip, port))
        return True
    except:
        return False

def choose_ip(ips):
    print("Available IP addresses for binding:")
    for idx, (iface, ip) in enumerate(ips):
        print(f"[{idx}] {ip} ({iface})")
    while True:
        choice = input("Select IP index: ")
        if choice.isdigit() and 0 <= int(choice) < len(ips):
            return ips[int(choice)][1]
        else:
            print("Invalid selection. Try again.")

def launch_server(server_name, target, ip):
    print(f"[+] Starting {server_name} server on {ip}...")
    thread = threading.Thread(target=target, args=(ip,), daemon=True)
    thread.start()

def main():
    ips = get_bindable_ips()
    if not ips:
        print("No available IPs found for binding.")
        sys.exit(1)

    selected_ip = choose_ip(ips)
    launch_server("FTP", ftp.start_ftp_server, selected_ip)
    launch_server("TFTP", tftp.start_tftp_server, selected_ip)
    launch_server("HTTP", http_server.start_http_server, selected_ip)

    print("[✔] All selected servers are running. Press Ctrl+C to stop.")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\n[!] Servers stopped.")

if __name__ == '__main__':
    main()
