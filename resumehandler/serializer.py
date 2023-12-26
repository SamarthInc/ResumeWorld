from rest_framework import serializers
from resumehandler.models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ('id', 'resumeText', 'uploadedDateTime')