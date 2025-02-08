import urllib.parse, urllib.request
import ssl
import json

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input('Enter-')
#http://py4e-data.dr-chuck.net/comments_42.json 2553
#http://py4e-data.dr-chuck.net/comments_2047108.json
print('Retieving',url)
fhand=urllib.request.urlopen(url,context=url)
data=fhand.read().decode()
print('retrieved:',len(data),'cahracters:',data[:20].replace('\n',' '))


js=json.loads(data)
count=len(js['comments'])
sum=0
for i in range(count):
    sum+=int(js['comments'][i]['count'])
print(sum)

