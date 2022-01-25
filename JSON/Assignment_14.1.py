import json
import urllib.request
count = 0

url = input("Enter url: ")
print ("Retrieving",url)
#uh = urllib.request().urlopen(url).read().decode()
uh =  urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
#data= uh.read()
#print('Retrieved', len(uh), 'characters')
info = json.loads(data)
for item in info["comments"]:
	#print item["count"]
	number = int(item["count"])
	count = count + number
print (count)
