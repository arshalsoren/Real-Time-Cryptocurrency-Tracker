import requests
import time
import pandas

# api from coincap.io
url="http://api.coincap.io/v2/assets?"
payload={}
headers={}
while(True):
    x=10
    d={'timestamp':[]}
    while x>0:
        d['timestamp'].append(time.strftime('%H:%M:%S'))    
        for i in range(10):
            response=requests.request("GET", url, headers=headers, data=payload)
            response_json=response.json()
            keys=['id','priceUsd']
            values=list(map(response_json['data'][i].get, keys))
            coin=values[0]
            price=values[1]
            if coin not in d:
                d[coin]=[price]
            else:
                d[coin].append(price)
        x-=1

    file=pandas.DataFrame.from_dict(d)
    file=file.to_csv('crypto.csv')
    print("Overwritten!")
    time.sleep(60*60)