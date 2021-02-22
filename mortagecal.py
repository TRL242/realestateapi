import requests

url = "https://realtor.p.rapidapi.com/mortgage/calculate"

querystring = {"hoi":"56.0","tax_rate":"1.2485549449920654","downpayment":"95000","price":"950000","term":"25","rate":"1.40"}

headers = {
    'x-rapidapi-key': "#",
    'x-rapidapi-host': "realtor.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

