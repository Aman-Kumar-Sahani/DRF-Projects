import requests
import json
URL = "http://127.0.0.1:8000/stucreate/"
data = {
        'name' : 'Aman',
        'roll' : 2,
        'city' : 'Gangtok'
    }
#coneverting python data to json
json_data = json.dumps(data)
#sending data so post requests
r = requests.post(url = URL,data =json_data)
data = r.json()
print(data)