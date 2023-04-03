from rest_framework import serializers
from .models import AboutCompanyTable, AddressesTable


class AboutCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCompanyTable
        fields = ["answer_id", "code", "name_ru", "text"]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressesTable
        fields = ['address_id', 'photo', 'address', 'link_2gis']
