#!/usr/bin/env python
import subprocess,re
TARGET_HOST = '8.8.8.8'
IP_REGEX = r"\((?:\d{1,3}\.{0,1}){0,4}\)"


traceroute_output = subprocess.run(['traceroute', TARGET_HOST], capture_output=True)
decoded_output = traceroute_output.stdout.decode('ascii')

matches_ip = [re.sub('\(|\)', '', ip) for ip in re.findall(IP_REGEX, decoded_output)]

print(decoded_output)
print(matches_ip)