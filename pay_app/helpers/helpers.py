import base64
import os
import requests

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
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    r = requests.get(api_url, headers=headers)
    access_token = r.json()["access_token"]

    return access_token

def simulate_c2b():
    access_token = get_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {
        "Authorization": "Bearer " + access_token
    }
    request = {
        "ShortCode": os.getenv("STK_SHORTCODE"),
        "CommandID": "CustomerPayBillOnline",
        "Amount": "2",
        "Msisdn": os.getenv("TEST_MSISDN"),
        "BillRefNumber": "0123456789"
    }
    response = requests.post(api_url, json=request, headers=headers)
    print("the response is", response.text)

simulate_c2b()