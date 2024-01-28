import datetime
from .models import Process
from .serializer import ProcessSerializer

def getProcess(id):
    process = Process.objects.get(id=id)
    serializer = ProcessSerializer(process, many=False)
    return serializer.data

def getProcessDto(id):
    return Process.objects.get(id=id)

def saveProcess(resumeText : str, jdText : str):
    return Process.objects.create(resumeText = resumeText, jdText= jdText ,uploadedDateTime = datetime.datetime.utcnow())