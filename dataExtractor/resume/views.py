import datetime
from dataExtractor.resume.models import Resume
from dataExtractor.resume.serializer import ResumeSerializer

# Create your views here.
def resumeData(id):
    resume = Resume.objects.get(id=id)
    serializer = ResumeSerializer(resume, many=False)
    return serializer.data    

def resumeDataDto(id):
    resume = Resume.objects.get(id=id)
    return resume

def saveResumeData(processId: int,  resumeText : str):
    Resume.objects.update_or_create(id = processId , 
                                    defaults={'text': resumeText, 'uploadedDateTime': datetime.datetime.utcnow()})