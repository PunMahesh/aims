from django import views
from django.urls import path
from farmer import views


urlpatterns = [
    path("farmer_kyc",views.kyc,name='farmer_kyc'),
 
]