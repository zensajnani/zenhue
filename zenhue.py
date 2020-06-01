#to make api calls
import requests
#to convert payload into data that the server accepts
import json
#to generate random hue value between 1 and 65535
import random
#to import ip of hue bridge and username from secrets.py
from secrets import *

#REST api
url = f"http://{ip}/api/{username}/groups/1/action"

#Controlling the bulb
def hue_state():

    #picks random colour
    hue = random.randrange(1, 65535)

    payload = json.dumps({"on":True, "sat":254, "bri":254,"hue":hue})

    #make put request
    r = requests.put(url, data=payload)
    print(r.text)

hue_state()