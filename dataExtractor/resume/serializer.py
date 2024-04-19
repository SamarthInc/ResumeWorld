from rest_framework import serializers

from dataExtractor.resume.models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ('id', 'text', 'uploadedDateTime')    
