# import json, requests

# url = 'http://maps.googleapis.com/maps/api/directions/json'

# #params = dict(
# #   
# #)

# resp = requests.get(url=url, params=params)
# data = json.loads(resp.text)
import http.client, requests

conn = http.client.HTTPSConnection("hackgt-api.ncrcloud.com")

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'nep-enterprise-unit': "SOME_STRING_VALUE",
    'nep-correlation-id': "SOME_STRING_VALUE",
    'nep-organization': "SOME_STRING_VALUE",
    'nep-application-key': "19c7b50447ef0a4e0147ef8067900000",
    'nep-service-version': "3.0.0-GA:1.0"
    }

conn.request("GET", "/catalog/item-prices/SOME_STRING_VALUE/SOME_STRING_VALUE", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))