import requests
import json
from pprint import pprint
import simplejson

resp = requests.get(' http://api.geonames.org/citiesJSON?north=44.1&south=-9.9&east=-22.4&west=55.2&lang=de&username=demo')
if resp.status_code != 200:
    # This means something went wrong.
  print(resp.status_code)
for todo_item in resp.json():
    print ( todo_item[0]  )

data = json.loads(resp.text)
print ( data)



r = requests.get('Https://api.github.com/users/harishvc/events/public')
for item in r.json():
    for c in item['payload'] :
        print(c )


#for item in data :

    #    print(data[0][1]   )

print (data['geonames'][1]["name"])