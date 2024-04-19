from django.shortcuts import render

# Create your views here.
import datetime
from dataExtractor.keyWords.models import Keywords
from dataExtractor.keyWords.serializer import KeywordsSerializer

# Create your views here.
def keywordsData(id):
    keyWords = Keywords.objects.get(id=id)
    serializer = KeywordsSerializer(keyWords, many=False)
    return serializer.data    

def keywordsDto(id):
    keyWords = Keywords.objects.get(id=id)
    return keyWords

def saveKeywordsData(processId: int, resumeKeyWords : str, jdKeyWords : str, skillsPresent : str, skillsAbsent : str):
    Keywords.objects.update_or_create(id = processId , defaults={'resumeKeyWords': resumeKeyWords,'jdKeyWords': jdKeyWords,'skillsPresent':skillsPresent, 'skillsAbsent':skillsAbsent, 'uploadedDateTime': datetime.datetime.utcnow()})