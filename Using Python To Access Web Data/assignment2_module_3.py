import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Get user inputs
url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))

# Repeat the process `count` times
print(f"Retrieving: {url}")
for i in range(count):
    # Open the URL and parse the HTML
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all anchor tags and get the one at the desired position
    tags = soup('a')
    url = tags[position - 1].get('href', None)  # -1 because positions are 1-based
    print(f"Retrieving: {url}")

# At the end, the `url` variable contains the last link
