
import requests, json


class Tm_Proxy():
    def __init__(self, key):
        self.key = key
        self.headers = {
            "content-type": "application/json",
            "accept": "application/json"
        }
        
    def getNewProxy(self):
        url = "https://tmproxy.com/api/proxy/get-new-proxy"
       
        data = json.dumps({
            "api_key": self.key,
            "sign": "string",
            "id_location": 0
        })
        result = requests.post(url=url, headers=self.headers, data=data)
        print(result.text)

    def getCurrentProxy(self):
        url = "https://tmproxy.com/api/proxy/get-current-proxy"
        data = json.dumps({
            "api_key": self.key,
        })
        result = requests.post(url=url, headers=self.headers, data=data)
        print(result.text)
Tm_Proxy(key="71d0a39a26860218827fea2fc297a97a").getCurrentProxy()