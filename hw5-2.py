import urllib.request
import json
url = "https://restcountries.eu/rest/v1/alpha/co"
web=urllib.request.urlopen(url)
content=web.read()
page=content.decode('utf-8')
json00 = json.loads(page)
country = input("Please enter the country CODE:")
found = 0
for i,ii in json00.items():
	if ( country == ii ):
		print(':::',json00['nativeName'],':::\n',':::',json00['capital'],':::\n')
		found = 1
		break
if( found==0 ):
	print("sorry!\n Didn't find it ")
	print("nativeName: ", json00['nativeName'],json00['capital'])
