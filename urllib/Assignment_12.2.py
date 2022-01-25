import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url: ")
count=int(input("Enter count: "))
position=int(input("Enter position: "))
#c=0
#while c<count :
for k in range(count) :
   html = urllib.request.urlopen(url).read()
   soup = BeautifulSoup(html,"html.parser")
   tags = soup('a')
   i = 0
   for tag in tags:
       i += 1
       if i == position:
        url=tag.get('href', None)
        break
       #c+=1
print ('The Last URL:', url)
