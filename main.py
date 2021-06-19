import json
import urllib.error
import urllib.parse
import urllib.request

googleurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

key = 'API_Key'

while True:
    address = input('Enter Location: ')
    if len(googleurl) < 1:
        break
    url = googleurl + urllib.parse.urlencode({'address': address},) + '&' + urllib.parse.urlencode({'key': key})
    print(url)

    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrived', len(data), 'character')

    try:
        content = json.loads(data)
    except:
        content = None

    #print(content)

    if content['status'] != 'OK' or 'status' not in content or not content:
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    #print(json.dumps(content, indent=4))

    lat = content['results'][0]['geometry']['location']['lat']
    lng = content['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = content['results'][0]['formatted_address']
    print(location)



