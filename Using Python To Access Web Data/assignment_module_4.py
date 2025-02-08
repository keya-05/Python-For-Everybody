from bs4 import BeautifulSoup
import urllib.request
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input('enter:')
fhand=urllib.request.urlopen(url)

soup=BeautifulSoup(fhand,'html.parser')
tags=soup.findAll('count')
sum=0
for tag in tags:
    content=int(tag.contents[0])
    sum+=content
print(sum)

