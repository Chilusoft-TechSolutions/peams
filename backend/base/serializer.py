from rest_framework import serializers
from base.models import *



class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('user', 'first_name', 'last_name', 'email')