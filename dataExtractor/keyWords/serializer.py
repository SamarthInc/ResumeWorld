from rest_framework import serializers

from dataExtractor.keyWords.models import Keywords

   
class KeywordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keywords
        fields = ('id', 'resumeKeyWords', 'jdKeyWords','skillsPresent','skillsAbsent', 'uploadedDateTime')    