import json

import requests
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
# @app.route('price')
def index():
    # getting response from the link
    response = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    a = json.loads(response.content)
    return render_template('index.html', articles=a['Data'])

# def price():
#     response = requests.get('https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH&tsyms=USD,EUR')
#     coinprice = json.loads(response.price)
#     return render_template('index.html', bitcoinprice=coinprice['Data'])
#

if __name__ == '__main__':
    app.run()
