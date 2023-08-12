from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import CustomUser, Profile
from .serializers import CustomUserSerializer, ProfileSerializer

    
# login api
@api_view(['POST'])
def login(request):
    user = get_object_or_404(CustomUser, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"detail": "Not found."}, status=status.HTTP_400_BAD_REQUEST)
    token, created = Token.objects.get_or_create(user=user)
    serializer = CustomUserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data})


# signup api
@api_view(['POST'])
def signup(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = CustomUser.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data})
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# test token api
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("Passed for {} with role {}".format(request.user.username, request.user.role))


# admin page api
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def administrator_page(request):
    if request.user.role != 'administrator':
        return Response({'message': 'you do not have access'})
    return Response("Hello admin {}".format(request.user.username))

# profile api
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# managers apis
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class ListCreateManagers(generics.ListCreateAPIView):
    serializer_class = CustomUserSerializer
    def get_queryset(self):
        if self.request.user.role == "administrator":
            return CustomUser.objects.filter(role="manager").values('username', 'email', 'role')
        else:
            return Response({'message': 'you do not have access'})

@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class ManagersDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUserSerializer
    def get_queryset(self):
        if self.request.user.role == "administrator":
            return CustomUser.objects.filter(role="mananger").values('username', 'email', 'role')
        else:
            return Response({'message': 'you do not have access'})

# data analysts apis
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class ListCreateAnalysts(generics.ListCreateAPIView):
    serializer_class = CustomUserSerializer
    def get_queryset(self):
        if self.request.user.role == "administrator":
            return CustomUser.objects.filter(role="data_analyst").values('username', 'email', 'role')
        else:
            return Response({'message': 'you do not have access'})

@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class AnalystsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUserSerializer
    def get_queryset(self):
        if self.request.user.role == "administrator":
            return CustomUser.objects.filter(role="data_analyst").values('username', 'email', 'role')
        else:
            return Response({'message': 'you do not have access'})

# farmers apis
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class ListCreateFarmers(generics.ListCreateAPIView):
    serializer_class = CustomUserSerializer
    def get_queryset(self):
        if self.request.user.role == "administrator":
            return CustomUser.objects.filter(role="farmer").values('username', 'email', 'role')
        else:
            return Response({'message': 'you do not have access'})

@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class FarmersDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUserSerializer
    def get_queryset(self):
        if self.request.user.role == "administrator":
            return CustomUser.objects.filter(role="farmer").values('username', 'email', 'role')
        else:
            return Response({'message': 'you do not have access'})
