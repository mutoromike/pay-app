import os
import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
from helpers import encode_data

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

def lipa_na_mpesa():
    access_token = get_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    time_data = datetime.now()
    time_stamp = time_data.strftime("%Y%m%d%H%M%S")
    data = os.getenv("SHORTCODE") + os.getenv("PASSKEY") + time_stamp
    request = {
        "BusinessShortCode": os.getenv("SHORTCODE"),
        "Password": encode_data(data),
        "Timestamp": time_stamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "10",
        "PartyA": os.getenv("PHONE_NUMBER"),
        "PartyB": os.getenv("SHORTCODE"),
        "PhoneNumber": os.getenv("PHONE_NUMBER"),
        "CallBackURL": "https://trypayment.com",
        "AccountReference": "1234567",
        "TransactionDesc": "Demo Payment"
    }

    response = requests.post(api_url, json=request, headers=headers)

    print (response.text)

lipa_na_mpesa()