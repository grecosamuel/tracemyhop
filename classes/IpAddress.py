#!/usr/bin/env python
import ipaddress

class IpAddress():
    
    def __init__(self, ip):
        try:
            self.ip = ipaddress.ip_address(ip)
        except Exception as e:
            raise ValueError(f"Ip provided is invalid, f{e}")
        self.ip_splitted = list(map(int, str(self.ip).split('.')))
    
    def get_ip_class(self):
        if self.isClassA():
            return "A"
        elif self.isClassB():
            return "B"
        elif self.isClassC():
            return "C"
        elif self.isClassD():
            return "D"
        elif self.isClassE():
            return "E"
        
    def isClassA(self):
        if (self.ip_splitted[0] >= 0 and self.ip_splitted[0] <= 127):
            return True
        return False
    
    def isClassB(self):
        if (self.ip_splitted[0] >=128 and self.ip_splitted[0] <= 191):
            return True
        return False

    def isClassC(self):
        if (self.ip_splitted[0] >= 192 and self.ip_splitted[0] <= 223):
            return True
        return False
        
    def isClassD(self):
        if (self.ip_splitted[0] >= 224 and self.ip_splitted[0] <= 239):
            return True
        return False
        
    def isClassE(self):
        if (self.ip_splitted[0] >= 240 and self.ip_splitted[0] <= 255):
            return True
        return False
    
    def __repr__(self) -> str:
        return self.ip.__str__

if __name__ == "__main__":
    str_ip = "127.0.0.1"
    ip = IpAddress(str_ip)
    print(f"{ip.ip} belongs to class {ip.find_ip_class()}")