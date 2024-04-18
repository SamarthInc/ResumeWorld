from rest_framework import serializers
from reportExtractor.models import DefaultScoreConfig, Score, ScoreConfig

   
class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ('id','configId' , 'keywordsScore' ,'experienceScore','educationScore','finalScore', 'uploadedDateTime') 


class ScoreConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreConfig
        fields = ('jobId', 'keywordsConfig' ,'experienceConfig','educationConfig', 'uploadedDateTime')

class DefaultScoreConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultScoreConfig
        fields = ('id','keywordsConfig' ,'experienceConfig','educationConfig', 'uploadedDateTime')        