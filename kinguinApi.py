import requests 
import time
import json
from config import api_config 

#endpoint uri
url = api_config.get("url")
headers={
     'X-Api-Key' : api_config.get("api_key"),
     'accept' : 'application/json'
}


#calculate pages in the server 
total_products = 107712 
page_size = 100
pages = (total_products // page_size) + (1 if total_products % page_size > 0 else 0 )

all_products = []

for page in range(1,3):
    params = { "pages" : page }
    response = requests.get(url+"/v1/products",headers=headers, params=params)
    data = response.json()

    #save products in list
    all_products.extend(data.get("results",[]))
    print(f"pagina {page} procesada correctamente")
    time.sleep(10)
   

# Save in json file
with open("productos.json", "w", encoding="utf-8") as json_file:
    json.dump(all_products, json_file, indent=4, ensure_ascii=False)

print(f"Se han guardado {len(all_products)} productos en 'productos.json'")