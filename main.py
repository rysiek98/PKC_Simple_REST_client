import json
from math import floor
import requests
from requests.auth import HTTPBasicAuth

def availableExchanges():
    url = "https://stockserver.azurewebsites.net/api/stockexchanges"
    response = requests.get(url)
    response.encoding = "utf-8"
    exchanges = customData(response.text)
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

def getClientFounds(username, password):
    url = "https://stockserver.azurewebsites.net/api/client"
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    response.encoding = "utf-8"
    object = response.json()
    funds = object['funds']
    return funds

def availableCompanies(exchange):
    url = f"https://stockserver.azurewebsites.net/api/shareslist/{exchange}"
    response = requests.get(url)
    response.encoding = "utf-8"
    companies = customData(response.text)
    return companies

def companyBuyPrice(exchange, company):
    url = f"https://stockserver.azurewebsites.net/api/shareprice/{exchange}?share={company}"
    response = requests.get(url)
    response.encoding = "utf-8"
    object = response.json()
    price = object[1]['price']
    return price

def companyBuyStocksAmount(exchange, company):
    url = f"https://stockserver.azurewebsites.net/api/shareprice/{exchange}?share={company}"
    response = requests.get(url)
    response.encoding = "utf-8"
    object = response.json()
    amount = object[1]['amount']
    return amount

def companySellPrice(exchanges, company):
    url = f"https://stockserver.azurewebsites.net/api/shareprice/{exchanges}?share={company}"
    response = requests.get(url)
    response.encoding = "utf-8"
    object = response.json()
    price = object[0]['price']
    return price

def buyStocks(exchanges, company, amount, price, username, password):
    url = "https://stockserver.azurewebsites.net/api/buyoffer"
    payload = "{\r\n   \"stockExchange\":\"%s\",\r\n    \"share\":\"%s\",\r\n    \"amount\":%s,\r\n    \"price\":%s\r\n}" % (exchanges, company, amount, price)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, auth=HTTPBasicAuth(username, password), headers=headers, data=payload)
    print(response.text)

def sellStocks(exchanges, company, amount,price, username, password):
    url = "https://stockserver.azurewebsites.net/api/selloffer"
    payload = "{\r\n   \"stockExchange\":\"%s\",\r\n    \"share\":\"%s\",\r\n    \"amount\":%s,\r\n    \"price\":%s\r\n}" % (exchanges, company, amount, price)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, auth=HTTPBasicAuth(username, password), headers=headers, data=payload)
    print(response.text)

def getHistory(username, password):
    url = "https://stockserver.azurewebsites.net/api/history"
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    response.encoding = "utf-8"
    print(response.text)
    object = response.json()
    return object

def customData(data):
    data = data.replace('"', '')
    data = data.replace('[', '')
    data = data.replace(']', '')
    data = data.split(',')
    return data

if __name__ == '__main__':

    username ="username"
    password = "password"

#Buy one stock

#     exchanges = availableExchanges()
#     company = availableCompanies(exchanges[0])
#     price = companyBuyPrice(exchanges[0], company[0])
#     buyStocks(exchanges[0], company[0], 1, price, username, password)
#     clientAccount(username, password)
#     getHistory(username, password)

#Buy 42 stocks

    # exchanges = availableExchanges()
    # maxLoop = 42
    #
    # for exchange in exchanges:
    #     if maxLoop == 0:
    #         break
    #     companies = availableCompanies(exchange)
    #     for company in companies:
    #         if maxLoop == 0:
    #             break
    #         if 150 > companyBuyPrice(exchange, company):
    #             price = companyBuyPrice(exchange, company)
    #             amount = companyBuyStocksAmount(exchange, company)
    #             for x in range(amount):
    #                 if maxLoop > 0:
    #                     buyStocks(exchange, company, 1, price, username, password)
    #                     maxLoop -= 1
    #                 else:
    #                     break
    # clientAccount(username, password)
    # getHistory(username, password)

#Buys stocks until it reduces funds to 89999-90001

    # exchanges = availableExchanges()
    # flag = True
    #
    # while flag:
    #      for exchange in exchanges:
    #       if not flag:
    #              break
    #       companies = availableCompanies(exchange)
    #
    #       for company in companies:
    #           founds = getClientFounds(username, password)
    #           founds = founds - 90000
    #           companyPrice = companyBuyPrice(exchange, company)
    #
    #           if founds > companyPrice and flag:
    #               maxAmount = floor(founds/companyPrice)
    #               amount = companyBuyStocksAmount(exchange, company)
    #               buyStocks(exchange, company, min(maxAmount, amount), companyPrice, username, password)
    #
    #           founds = getClientFounds(username, password)
    #
    #           if founds >= 89999 and founds <= 90001:
    #               flag = False
    #               break
    #           if founds < 89999:
    #               flag = False
    #               break

    clientAccount(username, password)
    with open('data.txt', 'w') as outfile:
        json.dump(getHistory(username, password), outfile)







