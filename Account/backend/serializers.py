from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class LoginObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod 
    def get_token(cls, user):
        token=super(LoginObtainPairSerializer, cls).get_token(user)
        
        token['username']=user.username
        
        return token


class RegistrationSerializer(serializers.ModelSerializer):

    email=serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password=serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )

    password2=serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = User
        fields=['username', 'first_name', 'last_name', 'phone', 'email', 'password', 'password2',]


    def validate(self, attrs):
        if  attrs['password2'] != attrs['password'] :
            return serializers.ValidationError('Olmadi')

        return attrs

    def create(self, validated_data):
        user=User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
            email=validated_data['email'],
            is_active=False
        )

        user.set_password(validated_data['password'])
        user.save()
        return user








