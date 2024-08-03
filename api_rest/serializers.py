from rest_framework import serializers
from .models import User, Tasks

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class

class UserTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['user_nickname', 'user_task']