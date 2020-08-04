import requests
import sys

url = 'http://40.124.104.53:5000/api'
req = requests.get("http://{}".format(url)).json()
if float(req.get('API').get('api')) == 1.2:
    print('OK')
    print(req)
else:
    print('Rollback sendo efetuado')
    print(req)
    sys.exit(4)