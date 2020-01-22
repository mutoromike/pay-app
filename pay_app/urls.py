from django.contrib import admin
from django.urls import path

from pay_app.apps.api_calls.views import ValidationC2BView, ConfirmationC2BView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/payments/c2b-validation/", ValidationC2BView.as_view(), name="c2bvalidation"),
    path("api/payments/c2b-confirmation/", ConfirmationC2BView.as_view(), name="c2bconfirmation")
]
