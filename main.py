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
    exchanges = customData(response.text)
    print(exchanges)
    return exchanges

def clientAccount(username, password):
    url = "https://stockserver.azurewebsites.net/api/client"
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    response.encoding = "utf-8"
    object = response.json()
    name = object['name']
    funds = object['funds']
    shares = object['shares']
    print('Name: '+name+" funds: "+str(funds)+" shares: "+str(shares))

def availableCompanies(exchange):
    url = f"https://stockserver.azurewebsites.net/api/shareslist/{exchange}"
    response = requests.get(url)
    response.encoding = "utf-8"
    companies = customData(response.text)
    print(companies)
    return companies

def companyBuyPrice(exchange, company):
    url = f"https://stockserver.azurewebsites.net/api/shareprice/{exchange}?share={company}"
    response = requests.get(url)
    response.encoding = "utf-8"
    object = response.json()
    time = object[0]['time']
    price = object[0]['price']
    amount = object[0]['amount']
    print('Time: ' + time + " price to buy: " + str(price) + " amount: " + str(amount))
    return price

def companySellPrice(exchanges, company):
    url = f"https://stockserver.azurewebsites.net/api/shareprice/{exchanges}?share={company}"
    response = requests.get(url)
    response.encoding = "utf-8"
    object = response.json()
    time = object[1]['time']
    price = object[1]['price']
    amount = object[1]['amount']
    print('Time: ' + time + " price to sell: " + str(price) + " amount: " + str(amount))

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

def customData(data):
    data = data.replace('"', '')
    data = data.replace('[', '')
    data = data.replace(']', '')
    data = data.split(',')
    return data

if __name__ == '__main__':
    availableExchanges()
    clientAccount("01143836@pw.edu.pl","TajneHaslo123")
    availableCompanies("Warszawa")
    companyBuyPrice("Warszawa", "11BIT")

    #Punk 3.1
    #exchanges = availableExchanges()
    #company = availableCompanies(exchanges[0])
    #price = companyBuyPrice(exchanges[0], company[0])
    #buyStocks(exchanges[0], company[0], 1, price, "01143836@pw.edu.pl", "TajneHaslo123")

    #Punkt 3.2
