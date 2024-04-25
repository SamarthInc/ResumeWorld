from reportExtractor.models import DefaultScoreConfig, Score, ScoreConfig
from reportExtractor.serializer import ScoreSerializer, ScoreConfigSerializer
import datetime

def scoreConfigDataDto(jobId):
    scoreConfig = ScoreConfig.objects.get(jobId=jobId)
    return scoreConfig
    
def scoreConfigData(jobId):
    scoreConfig = scoreConfigDataDto(jobId)
    serializer = ScoreConfigSerializer(scoreConfig, many=False)
    return serializer.data

def defaultScoreConfigDataDto(id):
    defaultScoreConfig = DefaultScoreConfig.objects.get(id=id)
    return defaultScoreConfig

def scoreData(id):
    all_scores = Score.objects.get(id=id)
    serializer = ScoreSerializer(all_scores, many=False)
    return serializer.data    

def scoreDataDto(id):
    all_scores = Score.objects.get(id=id)
    return all_scores

def multipleScoreData(ids):
    all_scores = Score.objects.filter(id__in=ids)
    serializer = ScoreSerializer(all_scores, many=True)
    return serializer.data    

def multipleScoreDataDto(ids):
    all_scores = Score.objects.filter(id__in=ids)
    return all_scores

def saveScoreData(processId: int, configId: int , keywordsScorePercentage:float, experienceScorePercentage : float, educationScorePercentage : float , finalScorePercentage : float):
    Score.objects.update_or_create(id = processId , 
                                   defaults={
                                       'configId' : configId,
                                       'keywordsScore': keywordsScorePercentage, 
                                       'experienceScore': experienceScorePercentage, 
                                       'educationScore': educationScorePercentage,
                                       'finalScore': finalScorePercentage,
                                       'uploadedDateTime': datetime.datetime.utcnow()}) 
    
def saveScoreConfigData(jobId: int, keywordsConfig:float, experienceConfig : float, educationConfig : float):
    ScoreConfig.objects.update_or_create(jobId = jobId , 
                                   defaults={
                                       'keywordsConfig': keywordsConfig, 
                                       'experienceConfig': experienceConfig, 
                                       'educationConfig': educationConfig,
                                       'uploadedDateTime': datetime.datetime.utcnow()}) 