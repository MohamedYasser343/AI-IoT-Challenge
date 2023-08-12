from rest_framework import serializers
from .models import Location, Esp_device, Esp_data

class Location_serializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class Esp_device_serializer(serializers.ModelSerializer):
    class Meta:
        model = Esp_device
        fields = '__all__'

class Esp_data_serializer(serializers.ModelSerializer):
    class Meta:
        model = Esp_data
        fields = '__all__'
