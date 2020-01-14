from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
# from rest_framework import status, exceptions

from pay_app.apps.api_calls.models import PaymentC2B
from pay_app.apps.api_calls.serializers import C2BPaymentSerializer, C2BConfirmationSerializer


class PaymentC2BView(CreateAPIView):

    query = PaymentC2B.objects.all()
    serilizer_class = C2BPaymentSerializer
    permission_classes = [AllowAny]


    def create(self, request):
        print("this is validation data", request.data)
        return Response({"data": "It worked"})


class ConfirmationC2BView(CreateAPIView):

    query = PaymentsC2B.objects.all()
    serilizer_class = C2BConfirmationSerializer
    permission_classes = [AllowAny]


    def create(self, request):
        print("this is confirmation data", request.data)
        return Response({"ResultDesc": 0})
# class ImplementLNMView(CreateAPIView):

#     def get_token():
#         data = os.getenv("CONSUMER_KEY") + ":" + os.getenv("CONSUMER_SECRET")

#         headers = {
#             "Authorization": "Basic " + encode_data(data),
#             "Content-Type": "aplication/json"
#         }
#         api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

#         r = requests.get(api_URL, headers=headers)
#         access_token = r.json()["access_token"]

#         return access_token

#     def lipa_na_mpesa():
#         access_token = get_token()
#         api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
#         headers = { "Authorization": "Bearer %s" % access_token }
#         time_data = datetime.now()
#         time_stamp = time_data.strftime("%Y%m%d%H%M%S")
#         data = os.getenv("SHORTCODE") + os.getenv("PASSKEY") + time_stamp
#         request = {
#             "BusinessShortCode": os.getenv("SHORTCODE"),
#             "Password": encode_data(data),
#             "Timestamp": time_stamp,
#             "TransactionType": "CustomerPayBillOnline",
#             "Amount": "10",
#             "PartyA": os.getenv("PHONE_NUMBER"),
#             "PartyB": os.getenv("SHORTCODE"),
#             "PhoneNumber": os.getenv("PHONE_NUMBER"),
#             "CallBackURL": "https://trypayment.com",
#             "AccountReference": "1234567",
#             "TransactionDesc": "Demo Payment"
#         }

#         response = requests.post(api_url, json=request, headers=headers)

#         print (response.text)