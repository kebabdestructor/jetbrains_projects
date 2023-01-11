import requests

cache = {}

source_currency = input().lower()
url = 'http://www.floatrates.com/daily/{}.json'.format(source_currency)
rates = requests.get(url).json()

if 'usd' in rates:
    cache.update({'usd': rates['usd']['rate']})
if 'eur' in rates:
    cache.update({'eur': rates['eur']['rate']})


def main():
    target_currency = input().lower()
    if not target_currency:
        return
    amount = float(input())
    result = 0
    print("Checking the cache...")
    try:
        result = cache[target_currency] * amount
        print("Oh! It is in the cache!")  
    except KeyError:
        print("Sorry, but it is not in the cache!")
        result = rates[target_currency]['rate'] * amount
        cache[target_currency] = rates[target_currency]['rate']
    print(f"You received {round(result, 2)} {target_currency.upper()}.")
    return main()
main()
