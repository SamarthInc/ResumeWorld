from rest_framework import serializers
from root.models import UploadRq


class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadRq
        fields = ('resume', 'jobDescription')