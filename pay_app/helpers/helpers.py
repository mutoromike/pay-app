import base64
import os
import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

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
        "BillRefNumber": "12345678"
    }
    try:
        response = requests.post(api_url, json=request, headers=headers)
    except:
        response = requests.post(api_url, json=request, headers=headers, verify=False)
    print("the response is", response.text)

simulate_c2b()

# def lipa_na_mpesa():
#     access_token = get_token()
#     api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
#     headers = { "Authorization": "Bearer %s" % access_token }
#     time_data = datetime.now()
#     time_stamp = time_data.strftime("%Y%m%d%H%M%S")
#     data = os.getenv("ONLINE_SHORTCODE") + os.getenv("PASSKEY") + time_stamp
#     request = {
#         "BusinessShortCode": os.getenv("ONLINE_SHORTCODE"),
#         "Password": encode_data(data),
#         "Timestamp": time_stamp,
#         "TransactionType": "CustomerPayBillOnline",
#         "Amount": "10",
#         "PartyA": os.getenv("PHONE_NUMBER"),
#         "PartyB": os.getenv("ONLINE_SHORTCODE"),
#         "PhoneNumber": os.getenv("PHONE_NUMBER"),
#         "CallBackURL": "https://trypayment.com",
#         "AccountReference": "1234567",
#         "TransactionDesc": "Demo Payment"
#     }

#     response = requests.post(api_url, json=request, headers=headers)

#     print (response.text)

# lipa_na_mpesa()