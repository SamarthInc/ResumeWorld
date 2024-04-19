from rest_framework import serializers

from dataExtractor.jobDescription.models import JobDescription


class JobDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDescription
        fields = ('id', 'text', 'uploadedDateTime')  
