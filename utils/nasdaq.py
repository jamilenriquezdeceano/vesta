import requests

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    "accept-language": "es-US,es;q=0.9,en-US;q=0.8,en;q=0.7,es-419;q=0.6",
}

def symbol_exists_on_nasdaq(symbol: str):
    url: str = "https://api.nasdaq.com/api/quote/{0}/info?assetclass=stocks".format(symbol)
    response = requests.get(url, headers =  HEADERS)
    data_json = response.json()
    if(data_json['data'] is None):
        return False
    return True