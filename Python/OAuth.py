import requests
import json

callbackCode = 'ec77fc21a263eb1c9b4ad5b564769014'

headers = {
    'X-API-Key': '1b3f55b792004e41b894bd035ab93b3d',
    'Content-Type': 'application/x-www-form-urlencoded'
}
payload = {
    'client_id': '22434',
    'grant_type': 'authorization_code',
    'code': callbackCode
}
# Adding empty header as parameters are being sent in payload
headers = {}

r = requests.post(
    url='https://www.bungie.net/Platform/App/OAuth/Token/',
    headers=headers,
    json=payload
)

# Committing this even though it doesn't work.
# There's something wrong with the JSON being sent
#print(r.status_code, r.reason)
#print(r.text)
#print(r.content)
'''
	var req = {
		method: 'POST',
		url: 'https://www.bungie.net/Platform/App/OAuth/Token/',
		headers: { 
			'Content-Type': 'application/x-www-form-urlencoded' 
		},
		data: { 
			client_id: '22434',
			grant_type: 'authorization_code',
			code: callbackCode
		}
	}
'''
