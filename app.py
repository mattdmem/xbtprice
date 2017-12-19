import requests
from flask import Flask
from flask_restful import Resource, Api
import re

app = Flask(__name__)
api = Api(app)

class Price(Resource):
    def get(self):

        result = requests.get('http://www.hl.co.uk/shares/shares-search-results/x/xbt-provider-ab-bitcoin-tracker-one',verify=False).content
        search = re.search('<span class="bid price-divide" >(.*)</span>', result)


        btc = search.group(1).replace(" SEK","")


        result = requests.get('http://www.hl.co.uk/shares/shares-search-results/x/xbt-provider-ab-ethereum-tracker-eur',verify=False).content
        search = re.search('<span class="bid price-divide" >(.*)</span>', result)


        eth = search.group(1).replace("&euro;","")

        data = { 'eth':eth, 'btc':btc }

        return data

api.add_resource(Price, '/price')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
