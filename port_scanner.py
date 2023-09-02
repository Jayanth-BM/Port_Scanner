import os

try:
    import socket
    import termcolor
except:
    os.system("pip install socket")
    os.system("pip install termcolor")


class PortScanner:
    def __init__(self, targets, general_ports):
        self.targets = targets
        self.ports = general_ports


    def scan_ports(self, target_ip, port_number):
        try:
            sock = socket.socket()
            sock.connect((target_ip, port_number))
            print(f"[+] The Port {port_number} is Opened")
        except:
            return False


    def convert_data(self):
        # If there is multiple number of targets
        if "," in self.targets:
            self.targets = [each_target.strip(' ') for each_target in self.targets.split(',')]
        else:
            pass
        
        # If there is any range of ports specified
        if "-" in self.ports:
            self.ports = self.ports.split("-") # Returns the list of two ports to iterate between them to get ports range
            self.ports = [int(each_ports) for each_ports in range(int(self.ports[0]), int(self.ports[1]))]
        elif "," in self.ports:
            self.ports = [int(each_ports) for each_ports in self.ports.split(",")]
        else:
            # For single port specified
            self.ports = int(self.ports)


    def start_scan(self):
        self.convert_data()
        if type(self.targets) == list and type(self.ports) == list:
            # Do this if there is multiple number of targets and multiple number of lists
            for each_targets in self.targets:
                total_ports_closed = 0
                print("\n")
                print(termcolor.colored(f"[*] Scanning Port for Target: {each_targets}", "green"))
                for each_ports in self.ports:
                    # Scan each ports sepcified to specific target
                    answer = self.scan_ports(each_targets, each_ports)
                    if answer == False:
                        total_ports_closed += 1
                print(termcolor.colored(f"[-] Total {total_ports_closed} are closed during scan", "red"))


        elif type(self.targets) == str and type(self.ports) == list:
            # Do this if there are multiple ports for one target
            total_ports_closed = 0
            print(termcolor.colored(f"[*] Scanning Port for Target: {self.targets}", "green"))
            for each_ports in self.ports:
                answer = self.scan_ports(self.targets, each_ports)
                if answer == False:
                    total_ports_closed += 1
            print(termcolor.colored(f"[-] Total {total_ports_closed} are closed during scan", "red"))


        elif type(self.targets) == list and type(self.ports) == int:
            # Do this if there are multiple targets and one port
            for each_targets in self.targets:
                print("\n")
                print(f"[*] Scanning Port for Target: {each_targets}")
                answer = self.start_scan(each_targets, self.ports)
                if answer == False:
                    total_ports_closed += 1
                print(f"[-] Port {self.ports} is not Opened for {each_targets}")


        elif type(self.targets) == str and type(self.ports) == int:
            # DO this if there is one target with one Port
            total_ports_closed = 0
            print("\n")
            print(termcolor.colored(f"[*] Scanning Port for Target: {self.targets}", "green"))
            answer = self.scan_ports(self.targets, self.ports)
            if answer == False:
                total_ports_closed += 1
            print(termcolor.colored(f"[-] Port {self.ports} is not Opened for {self.targets}", "red"))


        
