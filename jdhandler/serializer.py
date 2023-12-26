from rest_framework import serializers
from jdhandler.models import JobDecription


class JobDecriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDecription
        fields = ('id', 'jdText', 'uploadedDateTime')