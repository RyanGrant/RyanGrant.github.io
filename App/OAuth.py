'''
ReadDestinyInventoryAndVault

GET https://www.bungie.net/en/oauth/authorize?client_id=12345&response_type=code&state=6i0mkLx79Hp91nzWVeHrzHG4

POST https://www.bungie.net/platform/app/oauth/token/ HTTP/1.1
Authorization: Basic czZCaGRSa3F0MzpnWDFmQmF0M2JW
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code&code=SplxlOBeZQQYbYS6WxSbIA
'''

manifest_url = 'https://www.bungie.net/en/oauth/authorize?client_id=12345&response_type=code&state=6i0mkLx79Hp91nzWVeHrzHG4'
#get the manifest location from the json
r = requests.get(manifest_url)
manifest = r.json()
mani_url = 'http://www.bungie.net'+manifest['Response']['mobileWorldContentPaths']['en']
