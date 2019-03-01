import json

def get_data():
    import http.client
    conn = http.client.HTTPSConnection("api.coinmarketcap.com")
    conn.request("GET", "/v1/ticker/bitcoin/")
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))

def process():
    data = get_data()
    return data[0]