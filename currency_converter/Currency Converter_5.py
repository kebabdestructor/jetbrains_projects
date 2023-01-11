import requests
import json

currency_code = input()
url = 'http://www.floatrates.com/daily/{}.json'.format(currency_code)

#currencies = requests.get(url).json()
r = requests.get(url)
currencies = json.loads(r.text)

print(currencies)
print(currencies['usd'])
print(currencies['eur'])