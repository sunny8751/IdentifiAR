import http.client, requests, json

conn = http.client.HTTPSConnection("hackgt-api.ncrcloud.com")

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'Authorization': 'AccessToken eyJhbGciOiJFUzI1NiJ9.eyJtdGgiOlsicGFzc3dvcmQiXSwic3ViIjoiYWNjdDpvcmctMUBhZG1pbiIsIm5iZiI6MTUwNzk4NzIyNiwib3JnIjoiL29yZy0xLyIsImlzcyI6Ik5DUiIsInJscyI6ImVKeUZVMEZ5Z3pBTVBNTnIyaWNvUmlGcXdmTElJcG4wL3crcDdHQVNFeUFuc0x5NzNsbEpYNjNIMERiVW9WZlNlOXMwVjhJYml2MUFONUtucUFMS2RqWUFTaENLYUhlOWdGZjdya0g3OU9WaVpFOVdJZDliOFlJdzZPVlF5TEUvVThKR1ZEVldQRVFIRm9YQktpdzllUG9ESmZhVnJ6ZHVaZWlKQzhKWGlzWitYTVRwRkoxUStLd0h6bUhNTG44eEJicmg5c2xXRHVRcXZTbHV5ejRSU3lKVkpFZXZKR0NzUzFVN204a2krS2hTQlNVOFlPV3F3eXVIckJFRE9pM2hXaFRRUHlnL1BJbUhZUlYwVlRWWGtqUFRlOEJOUDd2emRSUFNkQUVoRE9SSzMxKzhyQ1ppVCtqVjhXN1QzOXMyUTAvcDBHRVkrRDVpWHBHQ2dFQWplT2h4Vlg5MGM1TGlhNzEySTlDUXA5OTNDWjV5TDl1M2dzNHRtWVVEV2pNY3VBc1dwRzBIaVBxTjZlN1I1TW91dWlrcWp4c29GRW5QWEptNnRqbFRhdG9mNXNETFBHZzN0dVd0eVRJQUE4NTI1RHU1c2Qzay9pRDhMTEJRaTlRQ1o4a1o3TkQvQVVxb0ZKOD0iLCJleHAiOjE1MDgwMTYwMjYsImlhdCI6MTUwNzk4NzIyNiwianRpIjoiZjA3MTcyODYtNTM3MC00NDIwLTg3MDgtMTlhNTA1NmQ2Mzk2In0.MEUCIQCiAjZIYJaAc9MM4Vk2tmV5zDk_4WSI7_6yxCjTeg4FJgIgXHkloZp7Qdk2oxvKt0BfocDltfsQhA9hIHiL4pXVAB8',
    # 'nep-organization': "SOME_STRING_VALUE",
    'nep-application-key': "8a82859f5ef21870015ef2fa5e5f0000"
    }

conn.request("GET", "/catalog/items/", headers=headers)

res = conn.getresponse()
data = res.read().decode("utf-8")

json_obj = json.loads(data)
pageContent = json_obj['pageContent']

print(json_obj['totalResults'])
print(pageContent[0]['version'])

