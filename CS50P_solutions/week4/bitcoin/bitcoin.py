import json
import sys
import requests
try:
    if len(sys.argv) < 1:
        raise Exception
    amount=float(sys.argv[1])
except:
    sys.exit("Command-line argument is not a number")
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
#print(json.dumps(response.json(), indent=2))

o = response.json()#storing json response in var called o
#for i in o["bpi"].keys():#key called USD
rate = (o["bpi"]["USD"]["rate"])
rate = float(rate.replace(',', ''))
value = rate * amount
value = ('{:,}'.format(value))
print("$",value,sep='')
