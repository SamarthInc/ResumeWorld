import datetime
from .models import Resume
from .serializer import ResumeSerializer

def getResume(pk):
    resume = Resume.objects.get(id=pk)
    serializer = ResumeSerializer(resume, many=False)
    return serializer.data

def saveResume(resumeText : str):
    Resume.objects.create(resumeText = resumeText ,uploadedDateTime = datetime.datetime.utcnow())