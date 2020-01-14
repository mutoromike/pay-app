import base64

def encode_data(data):
    encoded_data = base64.b64encode(data.encode("utf-8"))
    encoded_str = str(encoded_data, "utf-8")
    return encoded_str

def get_token():
    data = os.getenv("CONSUMER_KEY") + ":" + os.getenv("CONSUMER_SECRET")

    headers = {
        "Authorization": "Basic " + encode_data(data),
        "Content-Type": "aplication/json"
    }
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    r = requests.get(api_URL, headers=headers)
    access_token = r.json()["access_token"]

    return access_token