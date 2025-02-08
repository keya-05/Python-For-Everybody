import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url="http://py4e-data.dr-chuck.net/comments_2047105.html"
html=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,"html.parser")


tags=soup.find_all("span")
counts=0
for tag in tags:
    print('tag:',tag)
    content = tag.text.strip() if tag.text else "No Content"
    print('contents:',content)
    sum=int(content)
    counts+=sum

print("Extracted Contents:", counts)
