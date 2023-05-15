import requests
import json
import os

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r
jwt=os.environ['JWT_AUTH_TOKEN']
j=requests.get("https://kth.cnaas.sunet.se/api/v1.0/devices",auth=BearerAuth(jwt)).json()
l=[(x['management_ip'],x['hostname']) for x in j['data']['devices'] if x['device_type']=='ACCESS']
with open('cnaas-sw-list.json','w') as f:
   f.write(json.dumps(l))
