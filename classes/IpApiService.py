import requests, json

class IPAPIService():
    def __init__(self):
        self.base_path = "http://ip-api.com/"
        self.format = "json"
    def traceIP(self, ip):
        query = f"{self.base_path}{self.format}/{ip}"
        response = requests.get(query)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            raise Exception("Request IP Geolocation Error")