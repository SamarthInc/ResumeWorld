from rest_framework import serializers
from reportExtractor.models import Score, ScoreConfig

   
class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ('id','configId' , 'keywordsScore' ,'experienceScore','educationScore','finalScore', 'uploadedDateTime') 


class ScoreConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreConfig
        fields = ('id','keywordsConfig' ,'experienceConfig','educationConfig', 'uploadedDateTime')