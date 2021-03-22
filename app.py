from chalice import Chalice
from datetime import datetime
import requests
from chalicelib import API_KEY

app = Chalice(app_name='hellochalice')


@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/time')
def gettime():
    now = datetime.now()
    current_time = now.strftime("%D %H:%M:%S")
    return f"The time is {current_time}"


@app.route('/echo', methods=['POST'])
def echoback():
    request = app.current_request
    message = request.json_body
    return message


@app.route('/price/{symbol}')
def index(symbol):
    symbol = symbol.upper()
    url = f"https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest?symbol={symbol}"
    r = requests.get(url, headers={"X-CMC_PRO_API_KEY": API_KEY, "Content-Type":"application/json"})
    name = r.json()['data'][symbol][0]['name']
    price = r.json()['data'][symbol][0]['quote']['USD']['price']
    price = str('%.2f'%(float(price)))
    return f"{symbol}: The Price of {name} is {price}!"