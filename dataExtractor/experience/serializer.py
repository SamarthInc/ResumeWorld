from rest_framework import serializers

from dataExtractor.experience.models import Experience

   
class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ('id', 'text', 'uploadedDateTime')    
