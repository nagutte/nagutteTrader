import requests
import hmac
import hashlib

market = "BTC-LTC"
key = "1e105f4e2d3f4155847c12f632d3abc5"
secret = "323163c8eb71447e97b572fd4a588e44"
nonce = str(4658210)
quantity = str(1.00000000)
rate = str(.00050000)

def printlast():
    r = requests.get("https://bittrex.com/api/v1.1/public/getmarketsummary?market=" + market)
    j = r.json()
    f = j['result'][0]['Last']
    s = str('%.8f' % f)
    print(market + " Last: " + s)


def printbal():
    u = str("https://bittrex.com/api/v1.1/account/getbalances?apikey=" + key + "&nonce=" + nonce)
    b = bytes(u, 'utf-8')
    s = bytes(secret, 'utf-8')
    e = str(hmac.new(s, b, digestmod=hashlib.sha512).hexdigest())
    h = {'apisign': e}
    r = requests.post(u, headers=h)
    j = r.json()
    for i in range(len(j['result'])):
        print(j['result'][i]['Currency'] + ": " + str('%.8f' % j['result'][i]['Balance']))


def buylimit():
    u = str("https://bittrex.com/api/v1.1/market/buylimit" +
        "?apikey=" + key +
        "&nonce=" + nonce +
        "&market=" + market +
        "&quantity=" + quantity +
        "&rate=" + rate)
    b = bytes(u, 'utf-8')
    s = bytes(secret, 'utf-8')
    e = str(hmac.new(s, b, digestmod=hashlib.sha512).hexdigest())
    h = {'apisign': e}
    r = requests.post(u, headers=h)
    j = r.json()
    print(j)


def command():
    command = input("Input Command: \n")
    funcdict[command]()
    print()

funcdict = {
    'b': buylimit,
    'printlast': printlast,
    'printbal': printbal}

while True:
    command()
