from rest_framework import generics
# from django.shortcuts import get_object_or_404
# from rest_framework.response import Response
# from rest_framework.decorators import api_view

# from .utils import predict_data
from .models import Location, Esp_device, Esp_data
from .serializers import Location_serializer, Esp_device_serializer, Esp_data_serializer

class ListCreateLocation(generics.ListCreateAPIView):
    serializer_class = Location_serializer
    queryset = Location.objects.all()
    
class Location_detail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Location_serializer
    queryset = Location.objects.all()
    
    
class ListCreateEsp_device(generics.ListCreateAPIView):
    serializer_class = Esp_device_serializer
    queryset = Esp_device.objects.all()
    
class Esp_device_detail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Esp_device_serializer
    queryset = Esp_device.objects.all()
    

# get esp_data
class Esp_data_list(generics.ListAPIView):
    serializer_class = Esp_data_serializer
    queryset = Esp_data.objects.all()
    
    
# add esp_data
class Esp_data_create(generics.CreateAPIView):
    serializer_class = Esp_data_serializer
    queryset = Esp_data.objects.all()



# get esp_data by id      
class Esp_data_detail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Esp_data_serializer
    queryset = Esp_data.objects.all()


# get esp_data by esp_id
class Esp_id_data_detail(generics.ListAPIView):
    serializer_class = Esp_data_serializer

    def get_queryset(self):
        esp_id = self.kwargs['esp_id']
        return Esp_data.objects.filter(esp_id=esp_id)

# # predict data
# @api_view(['GET'])
# def esp_data_predictions(request):
#     data = Esp_data.objects.all()
#     predections = predict_data(data)
#     return Response(predections)