from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json

def databaseManagementInDjango():
    data = User.objects.get(pk='Luiz')                  #OBJECT

    data = User.objects.filter(user_age='23')           #QUERYSET

    data = User.objects.exclude(user_age='25')          #QUERYSET

    data.save()

    data.delete()