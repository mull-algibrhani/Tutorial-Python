import requests
import json
api_url = "https://www.emsifa.com/api-wilayah-indonesia/api/regencies/73.json"
response = requests.get(api_url)
print("=====DATA KABUPATEN======")
if response.status_code == 200:
    data = response.json()
    for d in data:
        id = d['id']
        prov_id = d['province_id']
        name = d['name']
        print(f"""
ID: {id}
PROV ID : {prov_id}
Nama Kab/Kota : {name}""")
else:
    print("error")
