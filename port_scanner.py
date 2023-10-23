import socket
import termcolor



class PortScanner:
    def __init__(self, targets, general_ports):
        self.targets = targets
        self.ports = general_ports
        self.target_dict = {}


    def scan_ports(self, target_ip, port_number):
        try:
            sock = socket.socket()
            sock.connect((target_ip, port_number))
            print(f"[+] The Port {port_number} is Opened")
            sock.close()
        except:
            return False


    def convert_data(self):
        # If there is multiple number of targets
        if "," in self.targets:
            self.targets = [each_target.strip(' ') for each_target in self.targets.split(',')]
        else:
            # Converting one element as list only
            self.targets = [self.targets]
            
        
        # If there is any range of ports specified
        if "-" in self.ports:
            self.ports = self.ports.split("-") # Returns the list of two ports to iterate between them to get ports range
            self.ports = [int(each_ports) for each_ports in range(int(self.ports[0]), int(self.ports[1]))]
        elif "," in self.ports:
            self.ports = [int(each_ports) for each_ports in self.ports.split(",")]
        else:
            # For single port specified 
            self.ports = [int(self.ports)]

        


    def start_scan(self):
        self.convert_data()
        for each_target in self.targets:
            # Starting the scan for each targets and specified ports
            total_closed_ports = 0
            print(termcolor.colored(f"[*] Scanning Port for target: {each_target}", "green"))
            for each_port in self.ports:
                answer = self.scan_ports(each_target, each_port)
                if answer == False:
                    total_closed_ports += 1
            print(termcolor.colored(f"[-] Total {total_closed_ports} Closed ports scanned for target..", "red"))
                

        
            


        
