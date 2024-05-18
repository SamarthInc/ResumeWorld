from rest_framework import serializers
from .models import UserProfile, EmailUpload

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'firstName','lastName', 'password','role')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user
    
class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model= EmailUpload
        fields=('emailId','message')