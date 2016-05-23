__author__ = 'cobedien'


import requests
import json

base_url = 'http://10.0.243.20/api/'
name_pwd = {'aaaUser': {'attributes': {'name': 'admin', 'pwd': 'cisco.123'}}}
json_credentials = json.dumps(name_pwd)

login_url = base_url + 'aaaLogin.json'
post_response = requests.post(login_url, data=json_credentials)
auth = json.loads(post_response.text)
login_attributes = auth['imdata'][0]['aaaLogin']['attributes']
auth_token = login_attributes['token']

cookies = {}
cookies['APIC-Cookie'] = auth_token

#sensor_url = base_url + 'topology/pod-1/node-202/sys/ch/supslot-1/sup/sensor-3.json'
#sensor_url = base_url + 'mo/topology/pod-1/node-202/sys/ch/supslot-1/sup/sensor-3/HDeqptTemp5min-0.json'
#sensor_url = base_url + 'mo/topology/HDfabricOverallHealth5min-0.json'
#sensor_url = base_url + 'mo/topology/pod-1/node-1.json'
#sensor_url = base_url + 'mo/uni/tn-THD/HDfvOverallHealth15min-0.json'
#sensor_url = base_url + 'node/class/fvTenant.json'
sensor_url = base_url + 'node/mo/topology/health.json'
print sensor_url


get_response = requests.get(sensor_url, cookies=cookies, verify=False)
data = get_response.json()
print data['imdata'][0]['fabricHealthTotal']['attributes']['cur']
#print data
#print data['imdata'][0]['fvTenant']['attributes']['name']