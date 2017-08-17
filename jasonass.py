import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    url = 'http://py4e-data.dr-chuck.net/comments_19182.json'

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    sum = 0
    #total_number = 0

    for comment in js["comments"]:
        sum += int(comment["count"])
        #total_number += 1
    print('Sum:', sum)
