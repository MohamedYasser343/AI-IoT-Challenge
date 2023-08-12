from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    crops_description = models.TextField(default="Any")
    
    def __str__(self):
        return self.name

class Esp_device(models.Model):
    mac_address = models.CharField(max_length=17, unique=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.mac_address

class Esp_data(models.Model):
    esp_id = models.ForeignKey(Esp_device, on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    light_intensity = models.DecimalField(max_digits=7, decimal_places=2)
    ph = models.DecimalField(max_digits=3, decimal_places=2)
    soil_moisture = models.DecimalField(max_digits=5, decimal_places=2)
    soil_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    water_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    flow_intensity = models.DecimalField(max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
