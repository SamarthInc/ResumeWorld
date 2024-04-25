from rest_framework import serializers
from root.models import BaseRs, UploadRq


class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadRq
        fields = ('resume', 'jobDescription')

class BaseRsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseRs
        fields = ('status', 'message')