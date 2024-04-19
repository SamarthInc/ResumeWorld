import datetime
from dataExtractor.education.models import Education
from dataExtractor.education.serializer import EducationSerializer



# Create your views here.
def educationData(id):
    education = Education.objects.get(id=id)
    serializer = EducationSerializer(education, many=False)
    return serializer.data    

def educationDataDto(id):
    education = Education.objects.get(id=id)
    return education

def saveEducationData(processId: int,educationText : str):
    Education.objects.update_or_create(id = processId , defaults={'text': educationText, 'uploadedDateTime': datetime.datetime.utcnow()})
    
