from django.urls import path
from .views import *
urlpatterns=[
    path('api/registration', RegisterView.as_view()),
    path('api/login', LoginView.as_view())
]