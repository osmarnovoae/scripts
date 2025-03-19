import requests
import time


url = "https://api.coingecko.com/api/v3/simple/price"
headers = {
    "accept":"application/json"
    }

params= {
     "ids":"bitcoin",
     "vs_currencies":"usd"
    }

#make response
while 1:
 
 response = requests.get(url,headers=headers, params=params)
 json=response.json()
 price= json.get("bitcoin").get("usd")
 print(price)
 #60 min represents 1m candle price
 time.sleep(60)
