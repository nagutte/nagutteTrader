import requests
import hmac
import hashlib

# /public/getmarkets
#     params: none

def getmarkets():
    u = "https://bittrex.com/api/v1.1/public/getmarkets"
    r = requests.get(u)
    j = r.json()
    MarketCurrency = j['result'][0]['MarketCurrency']
    BaseCurrency = j['result'][0]['BaseCurrency']
    MarketCurrencyLong = j['result'][0]['MarketCurrencyLong']
    BaseCurrencyLong = j['result'][0]['BaseCurrencyLong']
    MinTradeSize = j['result'][0]['MinTradeSize']
    MarketName = j['result'][0]['MarketName']
    IsActive = j['result'][0]['IsActive']
    Created = j['result'][0]['Created']
    Notice = j['result'][0]['Notice']
    IsSponsored = j['result'][0]['IsSponsored']
    LogoUrl = j['result'][0]['LogoUrl']
    print(MarketCurrency, BaseCurrency, MarketCurrencyLong, BaseCurrencyLong, MinTradeSize, MarketName, IsActive, Created, Notice, IsSponsored, LogoUrl)


# /public/getcurrencies
#     params: none

def getcurrencies():
    u = "https://bittrex.com/api/v1.1/public/getcurrencies"
    r = requests.get(u)
    j = r.json()
    Currency = j['result'][0]['Currency']
    CurrencyLong = j['result'][0]['CurrencyLong']
    MinConfirmation = j['result'][0]['MinConfirmation']
    TxFee = j['result'][0]['TxFee']
    IsActive = j['result'][0]['IsActive']
    CoinType = j['result'][0]['CoinType']
    BaseAddress = j['result'][0]['BaseAddress']
    print(Currency, CurrencyLong, MinConfirmation, TxFee, IsActive, CoinType, BaseAddress)


# /public/getticker
#     params: market*



# /public/getmarketsummaries
#     params: none
#
# /public/getmarketsummary
#     params: market*
#
# /public/getorderbook
#     params: market*, type* (buy, sell, both), depth (default 20, max 50)
#
# /public/getmarkethistory
#     params: market*
#
# /market/buylimit
#     params: market*, quantity*, rate*
#
# /market/selllimit
#     params: market*, quantity*, rate*
#
# /market/cancel
#     params: uuid*
#
# /market/getopenorders
#     params: market*
#
# /account/getbalances
#     params: none
#
# /account/getbalance
#     params: currency*
#
# /account/getdepositaddress
#     params: currency*
#
# /account/withdraw
#     params: currency*, quantity*, address*, paymentid (memo field)
#
# /account/getorder
#     params: uuid*
#
# /account/getorderhistory
#     params: market
#
# /account/getwithdrawalhistory
#     params: currency
#
# /account/getdeposithistory
#     params: currency
