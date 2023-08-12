from django.contrib import admin
from .models import Location, Esp_device, Esp_data

# Register your models here.
admin.site.register(Location)
admin.site.register(Esp_device)
admin.site.register(Esp_data)
