from reportExtractor.models import Score, ScoreConfig
from reportExtractor.serializer import ScoreSerializer, ScoreConfigSerializer
import datetime

def scoreConfigDataDto(id):
    scoreConfig = ScoreConfig.objects.get(id=id)
    return scoreConfig
    
def scoreConfigData(id):
    scoreConfig = scoreConfigDataDto(id)
    serializer = ScoreConfigSerializer(scoreConfig, many=False)
    return serializer.data

def scoreData(id):
    all_scores = Score.objects.get(id=id)
    serializer = ScoreSerializer(all_scores, many=False)
    return serializer.data    

def scoreDataDto(id):
    all_scores = Score.objects.get(id=id)
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