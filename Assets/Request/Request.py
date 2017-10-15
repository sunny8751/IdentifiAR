import http.client, requests, json, csv

# conn = http.client.HTTPSConnection("hackgt-api.ncrcloud.com")

# headers = {
#     'accept': "application/json",
#     'content-type': "application/json",
#     'Authorization': 'AccessToken eyJhbGciOiJFUzI1NiJ9.eyJtdGgiOlsicGFzc3dvcmQiXSwic3ViIjoiYWNjdDpvcmctMUBhZG1pbiIsIm5iZiI6MTUwNzk5NTk2MSwib3JnIjoiL29yZy0xLyIsImlzcyI6Ik5DUiIsInJscyI6ImVKeUZVMEZ5Z3pBTVBNTnIyaWNvUmlGcXdmTElJcG4wL3crcDdHQVNFeUFuc0x5NzNsbEpYNjNIMERiVW9WZlNlOXMwVjhJYml2MUFONUtucUFMS2RqWUFTaENLYUhlOWdGZjdya0g3OU9WaVpFOVdJZDliOFlJdzZPVlF5TEUvVThKR1ZEVldQRVFIRm9YQktpdzllUG9ESmZhVnJ6ZHVaZWlKQzhKWGlzWitYTVRwRkoxUStLd0h6bUhNTG44eEJicmg5c2xXRHVRcXZTbHV5ejRSU3lKVkpFZXZKR0NzUzFVN204a2krS2hTQlNVOFlPV3F3eXVIckJFRE9pM2hXaFRRUHlnL1BJbUhZUlYwVlRWWGtqUFRlOEJOUDd2emRSUFNkQUVoRE9SSzMxKzhyQ1ppVCtqVjhXN1QzOXMyUTAvcDBHRVkrRDVpWHBHQ2dFQWplT2h4Vlg5MGM1TGlhNzEySTlDUXA5OTNDWjV5TDl1M2dzNHRtWVVEV2pNY3VBc1dwRzBIaVBxTjZlN1I1TW91dWlrcWp4c29GRW5QWEptNnRqbFRhdG9mNXNETFBHZzN0dVd0eVRJQUE4NTI1RHU1c2Qzay9pRDhMTEJRaTlRQ1o4a1o3TkQvQVVxb0ZKOD0iLCJleHAiOjE1MDgwMjQ3NjEsImlhdCI6MTUwNzk5NTk2MSwianRpIjoiNTJjNDkxOGYtMjMyNS00MDAxLTkxMTktZjQyMjYyM2VhODE3In0.MEYCIQCs5FQIADP1RHoEGW0_g9MocbX5R3Fars_WbW5FLvRCWQIhAMYV7ekDyVDn8VrbWONsLYHaHH8-0t5xjySDCRL-TauA',
#     'nep-application-key': "8a82859f5ef21870015ef2fa5e5f0000"
#     }

# conn.request("GET", "/catalog/items/", headers=headers)

# res = conn.getresponse()
# data = res.read().decode("utf-8")

# json_obj = json.loads(data)
# pageContent = json_obj['pageContent']

# dataDict = {}
# aList = []
# for each in pageContent:
#     dataDict[each['itemId']['itemCode']] = [each['longDescription']['value']]
#     aList.append(each['packageIdentifiers'][0])


# headers2 = {
#     'accept': "application/json",
#     'content-type': "application/json",
#     'Authorization': 'AccessToken eyJhbGciOiJFUzI1NiJ9.eyJtdGgiOlsicGFzc3dvcmQiXSwic3ViIjoiYWNjdDpvcmctMUBhZG1pbiIsIm5iZiI6MTUwNzk5NTk2MSwib3JnIjoiL29yZy0xLyIsImlzcyI6Ik5DUiIsInJscyI6ImVKeUZVMEZ5Z3pBTVBNTnIyaWNvUmlGcXdmTElJcG4wL3crcDdHQVNFeUFuc0x5NzNsbEpYNjNIMERiVW9WZlNlOXMwVjhJYml2MUFONUtucUFMS2RqWUFTaENLYUhlOWdGZjdya0g3OU9WaVpFOVdJZDliOFlJdzZPVlF5TEUvVThKR1ZEVldQRVFIRm9YQktpdzllUG9ESmZhVnJ6ZHVaZWlKQzhKWGlzWitYTVRwRkoxUStLd0h6bUhNTG44eEJicmg5c2xXRHVRcXZTbHV5ejRSU3lKVkpFZXZKR0NzUzFVN204a2krS2hTQlNVOFlPV3F3eXVIckJFRE9pM2hXaFRRUHlnL1BJbUhZUlYwVlRWWGtqUFRlOEJOUDd2emRSUFNkQUVoRE9SSzMxKzhyQ1ppVCtqVjhXN1QzOXMyUTAvcDBHRVkrRDVpWHBHQ2dFQWplT2h4Vlg5MGM1TGlhNzEySTlDUXA5OTNDWjV5TDl1M2dzNHRtWVVEV2pNY3VBc1dwRzBIaVBxTjZlN1I1TW91dWlrcWp4c29GRW5QWEptNnRqbFRhdG9mNXNETFBHZzN0dVd0eVRJQUE4NTI1RHU1c2Qzay9pRDhMTEJRaTlRQ1o4a1o3TkQvQVVxb0ZKOD0iLCJleHAiOjE1MDgwMjQ3NjEsImlhdCI6MTUwNzk5NTk2MSwianRpIjoiNTJjNDkxOGYtMjMyNS00MDAxLTkxMTktZjQyMjYyM2VhODE3In0.MEYCIQCs5FQIADP1RHoEGW0_g9MocbX5R3Fars_WbW5FLvRCWQIhAMYV7ekDyVDn8VrbWONsLYHaHH8-0t5xjySDCRL-TauA',
#     'nep-application-key': "8a82859f5ef21870015ef2fa5e5f0000",
#     'nep-enterprise-unit': 'eafe5b77b5594e9ab575ed4b41d6ee37'
#     }

# for each in aList:
#     conn.request("GET", "/catalog/item-details/" + each, headers=headers2)

#     res = conn.getresponse()
#     data = res.read().decode("utf-8")

#     json_obj = json.loads(data)
#     itemInfo = json_obj['item']
#     priceInfo = json_obj['itemPrices']

#     dataDict[itemInfo['itemId']['itemCode']].append(priceInfo[0]['price'])

#tags from Unity output
holoInput = "bottle"


bList = []
with open("catalog.csv", "r") as file:
    reader = csv.reader(file, delimiter = ",")
    for each in reader:
        bList.append([each[1].lower().strip(),"$" + str(each[3]), each[0]])


cList = []
for each in bList[1:len(bList)]:
    cList.append(each[0].split(" "))

suggestedItems = []
for i, each in enumerate(cList):
    if holoInput.lower().strip() in each:
        suggestedItems.append(bList[i + 1][2])

tagList = ['banana', 'yellow', 'sitting','fruit']
suggestedItems = []
for each in tagList:
    jsonDict = {}
    for i, item in enumerate(cList):
        if each.lower().strip() in item:
            suggestedItems.append(bList[i + 1][0])

itemDict = {}
for each in suggestedItems:
    if each in itemDict.keys():
        itemDict[each] += 1
    else:
        itemDict[each] = 1

maxNum = max(itemDict.values())

items = []
for i in itemDict:
    if itemDict[i] == maxNum:
        items.append(i)


jsonDict2 = {}
for each in items:
    for item in bList:
        if each == item[0]:
            new = suggestedItems[0:5]
            if each in new:
                new.remove(each)
                new.append(suggestedItems[6])
            jsonDict2[each] = []
            jsonDict2[each].append({
                'longDescription': item[0],
                'price': item[1],
                'suggestedItems': new
            })

print(json.dumps(jsonDict2))
