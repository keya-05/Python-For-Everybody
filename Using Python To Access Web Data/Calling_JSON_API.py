import urllib.parse, urllib.request
import ssl,json

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

while True:
    address=input('Enter location-')
    if len(address)<1:
        break
    address=address.strip()
    parms=dict()
    parms['q']=address

    url= 'http://py4e-data.dr-chuck.net/opengeo?' +urllib.parse.urlencode(parms)
    print('retrieving url',url)
    fhand=urllib.request.urlopen(url,context=ctx)
    data=fhand.read().decode()
    print('retrieved',len(data))

    try:
        js=json.loads(data)
    except:
        js=None
    if not js or 'features' not in js:
        print('==== Download error ===')
        print(data)
        break
    if len(js['features']) == 0:
        print('==== Object not found ====')
        print(data)
        break


    plus_code=js['features'][0]['properties']['plus_code']
    print('plus code:',plus_code)



