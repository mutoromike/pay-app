from django.contrib import admin
from django.urls import path

from pay_app.apps.api_calls.views import ValidationC2BView, ConfirmationC2BView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/validation/", ValidationC2BView.as_view(), name="validation"),
    path("api/v1/confirmation/", ConfirmationC2BView.as_view(), name="confirmation")
]
