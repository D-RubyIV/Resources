


import requests, json


class Ts_Proxy():
    def __init__(self, key):
        self.key = key
        self.headers = {
            "content-type": "application/json",
            "accept": "application/json"
        }
        
    def getNewProxy(self):
        url = "http://proxy.tinsoftsv.com/api/changeProxy.php"
        params = {
           "key": self.key,
           "location": 0 #random
        }
        result = requests.post(url=url, headers=self.headers, params=params)
        print(result.text)

    def getCurrentProxy(self):
        url = "http://proxy.tinsoftsv.com/api/getProxy.php"
        params = {
           "key": self.key,
        }
        result = requests.post(url=url, headers=self.headers, data=params)
        print(result.text)

Ts_Proxy(key="TLdjT0uJuRt4GQ5TlfITVbLXdklrBmABYPhdlH").getCurrentProxy()