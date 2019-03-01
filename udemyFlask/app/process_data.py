import json

def get_data(query_string):
    import http.client
    conn = http.client.HTTPSConnection("api.coinmarketcap.com")
    conn.request("GET", "{}".format(query_string))
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))

def process(enteredCoin):
    data = get_data("/v1/ticker/{}/".format(enteredCoin))
    return data[0]

def calculate_coin(price_usd):
    return(float(price_usd) > 40)

def process_coins():
    data = get_data("/v1/ticker/?limit=10")
    all_coins = []
    for coin in data:
        coin["isover40"] = calculate_coin(coin["price_usd"])
        all_coins.append(coin)
    return all_coins
