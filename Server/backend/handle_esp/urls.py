from django.urls import path
from . import views

urlpatterns = [
    path('', views.Esp_data_list.as_view(), name='esp_data_list'),
    path('add/', views.Esp_data_create.as_view(), name='esp_data_create'),
    path('<int:pk>/', views.Esp_data_detail.as_view(), name='esp_data_detail'),
    path('esp_id/<int:esp_id>/', views.Esp_id_data_detail.as_view(), name='esp_id_data_detail'),
    
    path('esp_devices/', views.ListCreateEsp_device.as_view(), name='esp_device'),
    path('esp_devices/<int:pk>', views.Esp_device_detail.as_view(), name='esp_detail'),
    
    path('location/', views.ListCreateLocation.as_view(), name='location'),
    path('location/<int:pk>', views.Location_detail.as_view(), name='location_detail'),
    
    # path('predictions/', views.esp_data_predictions, name='esp_data_predictions'),
]
