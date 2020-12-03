# Dane rejestracja
# "number":"300493",
# "username":"01143836@pw.edu.pl",
# "password":"TajneHaslo123"


import requests
import http.client
from requests.auth import HTTPBasicAuth
import mimetypes


def clientAccount():
    url = "https://stockserver.azurewebsites.net/api/client"
    response = requests.get(url, auth=HTTPBasicAuth('01143836@pw.edu.pl', 'TajneHaslo123'))
    response.encoding = "utf-8"
    object = response.json()
    name = object['name']
    funds = object['funds']
    shares = object['shares']
    print('Name: '+name+" funds: "+str(funds)+" shares: "+str(shares))


if __name__ == '__main__':
    conn = http.client.HTTPSConnection("stockserver.azurewebsites.net")
    payload = ''
    headers = {}
    conn.request("GET", "/api/stockexchanges", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    clientAccount()