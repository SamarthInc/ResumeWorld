from .models import JobDecription
from .serializer import JobDecriptionSerializer

def getJd(pk):
    users = JobDecription.objects.get(id=pk)
    serializer = JobDecriptionSerializer(users, many=False)
    return serializer.data

def saveJD(jdText : str):
    JobDecription.objects.create(jdText=jdText)
