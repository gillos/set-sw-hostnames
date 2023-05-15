import requests,json,os
with open('cnaas-sw-list.json') as f:
   j=json.loads(f.read())
for (ip,name) in j:
   x=requests.get("https://sysadm.lan.kth.se/api/v0/set_hostname",params={'ipaddress':ip,'hostname':name},headers={'apilabel':os.environ['KIDDOW_KEY'],'apisecret':os.environ['KIDDOW_SECRET']})
   print(x)
