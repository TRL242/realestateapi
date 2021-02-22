import requests
import json

url = "https://realtor.p.rapidapi.com/properties/v2/list-sold"

querystring = {"city":"Victoria, British Columbia","offset":"0","state_code":"BC","limit":"200","sort":"sold_date"}

headers = {
    'x-rapidapi-key': "#",
    'x-rapidapi-host': "realtor.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
print(json.loads(response.text))

# sold_house_data = response.json()
# sold_houses = sold_house_data["Results"]["Id"]
# #print(sold_houses)
# for house in sold_houses:
#     print(house)