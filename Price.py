import requests
import json
import time

request_address = 'https://api.coindesk.com/v1/bpi/currentprice/usd.json'
Price_Cache = 0

while True == True:
        time.sleep(5)
        try:
            result = requests.get(request_address)
        except:
            print('Connection lost...')
            print()
            continue

        if result.status_code != 200:
            print('Error...')
            print()
            continue
        Price_Info = json.loads(result.text)
        Price_Rate = Price_Info['bpi']['USD']['rate']
        Price_Currency_Code = Price_Info['bpi']['USD']['code']
        Price_Time = Price_Info['time']['updated']
        if Price_Rate == Price_Cache:
            continue
        Price_Cache = Price_Rate
        print(f'{Price_Rate}')
        print()