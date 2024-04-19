import datetime
from dataExtractor.experience.models import Experience
from dataExtractor.experience.serializer import ExperienceSerializer

# Create your views here.
def experienceData(id):
    experience = Experience.objects.get(id=id)
    serializer = ExperienceSerializer(experience, many=False)
    return serializer.data    

def experienceDataDto(id):
    experience = Experience.objects.get(id=id)
    return experience

def saveExperienceData(processId: int, experienceText : str):
    Experience.objects.update_or_create(id = processId , defaults={'text': experienceText, 'uploadedDateTime': datetime.datetime.utcnow()})
