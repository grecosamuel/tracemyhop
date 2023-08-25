#!/usr/bin/env python
import subprocess,re
from classes.IpApiService import IPAPIService
from classes.IpAddress import IpAddress

TARGET_HOST = input("Host target (ip address or domain): ")
IP_REGEX = r"\((?:\d{1,3}\.{0,1}){0,4}\)"


traceroute_output = subprocess.run(['traceroute', TARGET_HOST], capture_output=True)
decoded_output = traceroute_output.stdout.decode('ascii')

matches_ip = [re.sub('\(|\)', '', ip) for ip in re.findall(IP_REGEX, decoded_output)]

api = IPAPIService()

for hop, str_ip in enumerate(matches_ip):
    ip = IpAddress(str_ip)
    ip_geolocation = api.traceIP(str_ip)
    api.pprint_json_response(response=ip_geolocation, hop=hop)