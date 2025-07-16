import socket
import netifaces

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