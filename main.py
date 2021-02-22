import requests
import os
print(os.environ.get("REALTOR_APIKEY"))
# url = "https://realtor-canadian-real-estate.p.rapidapi.com/properties/get-statistics"
#
# querystring = {"Latitude":"48.454453409964245","Longitude":"-123.4444933661592","CultureId":"1"}
#
# headers = {
#     'x-rapidapi-key': "####",
#     'x-rapidapi-host': "realtor-canadian-real-estate.p.rapidapi.com"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.text)