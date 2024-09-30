from rest_framework.serializers import ModelSerializer
from .models import Profile
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileSerializer(ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['full_name', 'dob', 'user']
