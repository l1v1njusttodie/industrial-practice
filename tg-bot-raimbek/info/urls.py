from django.urls import path
from .views import AboutCompanyDetails, AboutCompanyByQueryAPIView, AddressDetails, AddressByQueryAPIView

urlpatterns = [

    path("about/", AboutCompanyDetails.as_view(), name="about"),
    path('', AboutCompanyByQueryAPIView.as_view()),
    path("addresses/", AddressDetails.as_view(), name="about"),
    path('address/', AddressByQueryAPIView.as_view(), name="address"),

]
