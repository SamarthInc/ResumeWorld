from rest_framework import serializers
from processHandler. models import Process


class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = ('id', 'resumeText', 'jdText', 'uploadedDateTime')