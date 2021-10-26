import requests
import json
from datetime import datetime

response = requests.get('http://api.open-notify.org/astros.json')
print(response.status_code)


print(response.json)
def json_print(obj): 
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
json_print(response.json())

parametros_madrid = {
  'lat': 40.4167,
  'lon': -3.70325
}

response = requests.get('http://api.open-notify.org/iss-pass.json', params=parametros_madrid)
json_print(response.json())

pass_times = response.json()['response']
json_print(pass_times)

risetimes = []

for d in pass_times: 
  time = d['risetime']
  risetimes.append(time)

print(risetimes)

times = []

for rt in risetimes:
  time = datetime.fromtimestamp(rt)
  times.append(time)
  print(time)
