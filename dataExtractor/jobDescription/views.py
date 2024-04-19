import datetime

from dataExtractor.jobDescription.models import JobDescription
from dataExtractor.jobDescription.serializer import JobDescriptionSerializer

def jdData(id):
    users = JobDescription.objects.get(id=id)
    serializer = JobDescriptionSerializer(users, many=False)
    return serializer.data   

def jdDataDto(id):
    return JobDescription.objects.get(id=id)

def saveJdData(processId: int, jdText : str):
    JobDescription.objects.update_or_create(id = processId , defaults={'text': jdText, 'uploadedDateTime': datetime.datetime.utcnow()})