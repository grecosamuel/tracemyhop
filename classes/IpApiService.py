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
        
    def pprint_json_response(self, response, hop=None):
        try:
            if hop != None: print(f"[HOP n.{hop}] GEOLOCATION INFO ABOUT {response['query']}")
            else: print(f"GEOLOCATION INFO ABOUT {response['query']}")
            for k, v in response.items(): 
                if k != "query": print(f"\t{k} -> {v}") 
        except KeyError as e:
            raise ValueError("response in input is invalid")
        
if __name__ == "__main__":
    api = IPAPIService()
    print(api.traceIP("8.8.8.8"))
