from rest_framework import serializers

from dataExtractor.education.models import Education


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('id', 'text', 'uploadedDateTime')       
