# Dane rejestracja
# "number":"300493",
# "username":"01143836@pw.edu.pl",
# "password":"TajneHaslo123"


import requests
from requests.auth import HTTPBasicAuth

def availableExchanges():
    url = "https://stockserver.azurewebsites.net/api/stockexchanges"
    response = requests.get(url)
    response.encoding = "utf-8"
    print(response.text)

def clientAccount(username, password):
    url = "https://stockserver.azurewebsites.net/api/client"
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    response.encoding = "utf-8"
    object = response.json()
    name = object['name']
    funds = object['funds']
    shares = object['shares']
    print('Name: '+name+" funds: "+str(funds)+" shares: "+str(shares))

def availableCompanies(exchanges):
    url = f"https://stockserver.azurewebsites.net/api/shareslist/{exchanges}"
    response = requests.get(url)
    response.encoding = "utf-8"
    print(response.text)

def companyPrice(exchanges, company):
    url = f"https://stockserver.azurewebsites.net/api/shareprice/{exchanges}?share={company}"
    response = requests.get(url)
    response.encoding = "utf-8"
    print(response.text)

def buyStocks(exchanges, company, amount, price, username, password):
    url = "https://stockserver.azurewebsites.net/api/buyoffer"
    data = {
        "stockExchange": f"{exchanges}",
        "share": f"{company}",
        "amount": amount,
        "price": price
    }
    response = requests.post(url, data, auth=HTTPBasicAuth(username, password))
    response.encoding = "utf-8"
    print(response.text)

def sellStocks(exchanges, company, amount,price, username, password):
    url = "https://stockserver.azurewebsites.net/api/selloffer"
    data = {
        "stockExchange": f"{exchanges}",
        "share": f"{company}",
        "amount": amount,
        "price": price
    }
    response = requests.post(url, data, auth=HTTPBasicAuth(username, password))
    response.encoding = "utf-8"
    print(response.text)

if __name__ == '__main__':
    availableExchanges()
    clientAccount("01143836@pw.edu.pl","TajneHaslo123")
    availableCompanies("Warszawa")
    companyPrice("Warszawa", "11BIT")