#!/usr/bin/env python
import ipaddress

class IpAddress():
    
    def __init__(self, ip):
        try:
            self.ip = ipaddress.ip_address(ip)
        except Exception as e:
            raise ValueError(f"Ip provided is invalid, f{e}")
        self.ip_splitted = list(map(int, str(self.ip).split('.')))
    
    def find_ip_class(self):
        if(self.ip_splitted[0] >= 0 and self.ip_splitted[0] <= 127):
            return "A"
        elif(self.ip_splitted[0] >=128 and self.ip_splitted[0] <= 191):
            return "B"
        elif(self.ip_splitted[0] >= 192 and self.ip_splitted[0] <= 223):
            return "C"
        elif(self.ip_splitted[0] >= 224 and self.ip_splitted[0] <= 239):
            return "D"
        else:
            return "E"


if __name__ == "__main__":
    str_ip = "127.0.0.1"
    ip = IpAddress(str_ip)
    print(f"{ip.ip} belongs to class {ip.find_ip_class()}")