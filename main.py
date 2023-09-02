from port_scanner import PortScanner
import termcolor

print(termcolor.colored(f"[*] Scanning sometimes takes a while wait for some time...", "blue"))
targets = input("[+] Please Specify the targets to Scan: ")
ports = input("[+] Please Specify the port range or port to scan(1-100 or 1,2,5,6): ")
try:
    scanner = PortScanner(targets=targets, general_ports=ports)
    scanner.start_scan()
except Exception as e:
    pass
