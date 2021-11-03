from django.shortcuts import render
from .models import User
from rest_framework import generics
from backend.serializers  import RegistrationSerializer, LoginObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.

class LoginView(TokenObtainPairView):
    serializer_class=LoginObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class= RegistrationSerializer