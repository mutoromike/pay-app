from rest_framework import serializers
from pay_app.apps.api_calls.models import PaymentC2B

class C2BValidationSerializer(serializers.ModelSerializer):

    model = PaymentC2B
    fields = "__all__"


class C2BConfirmationSerializer(serializers.ModelSerializer):

    model = PaymentC2B
    fields = "__all__"