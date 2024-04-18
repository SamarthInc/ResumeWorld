import datetime
from .models import Process, Resume, JobDescription
from .serializer import ExtendedProcessSerializer, JobDescriptionSerializer, ProcessSerializer, ResumeSerializer
from django.db.models import Q

def getProcess(id):
    process = Process.objects.get(id=id)
    serializer = ProcessSerializer(process, many=False)
    return serializer.data

def getProcessDto(id):
    return Process.objects.get(id=id)

def getExtendedProcessesByUserId(userId):
    print(userId)
    process = Process.objects.filter(userId=userId)
    serializer = ExtendedProcessSerializer(process, many=True)
    return serializer.data

def getExtendedProcessDto(userId):
    processes = Process.objects.filter(userId=userId)
    return processes

def getJobDescription(id):
    jobDescription = JobDescription.objects.get(id=id)
    serializer = JobDescriptionSerializer(jobDescription, many=False)
    return serializer.data

def getJobDescriptionDto(id):
    return JobDescription.objects.get(id=id)

def getJobDescriptionsByUserId(userId):
    jobDescription = JobDescription.objects.filter(userId=userId)
    serializer = JobDescriptionSerializer(jobDescription, many=True)
    return serializer.data

def getJobDescriptionsByUserIdDto(userId):
    return JobDescription.objects.filter(userId=userId)

def getResume(id):
    resume = Resume.objects.get(id=id)
    serializer = ResumeSerializer(resume, many=False)
    return serializer.data

def getResumeDto(id):
    return Resume.objects.get(id=id)

def getResumesByUserId(userId):
    resume = Resume.objects.filter(userId=userId)
    serializer = ResumeSerializer(resume, many=True)
    return serializer.data

def getResumesByUserIdDto(userId):
    return Resume.objects.filter(userId=userId)

def saveProcess( userId : int, jdText : str, jdTitle: str , resumeText: str, fileName : str ):
    saveResume = Resume.objects.create(userId = userId, resumeText = resumeText, fileName= fileName ,uploadedDateTime = datetime.datetime.utcnow());
    saveJd = JobDescription.objects.create(userId = userId, jdText = jdText, jdTitle= jdTitle ,uploadedDateTime = datetime.datetime.utcnow());
    return Process.objects.create(userId = userId, reqId = saveJd.reqId, profileId= saveResume.profileId ,uploadedDateTime = datetime.datetime.utcnow())

def saveProcessWithExistingData( userId : int, reqId : int, profileId: int ):
    return Process.objects.create(userId = userId, reqId = reqId, profileId= profileId ,uploadedDateTime = datetime.datetime.utcnow())

def saveJobDescription( userId : int, jdText : str, jdTitle: str ):
    return JobDescription.objects.create(userId = userId, jdText = jdText, jdTitle= jdTitle ,uploadedDateTime = datetime.datetime.utcnow());

def saveResume( userId : int, resumeText: str, profileTitle : str, fileName : str ):
    return Resume.objects.create(userId = userId, resumeText = resumeText, profileTitle = profileTitle , fileName= fileName ,uploadedDateTime = datetime.datetime.utcnow());

def deleteJobDescription(userId : int, reqId: int):
    return JobDescription.objects.filter(reqId=reqId, userId=userId).delete()

def deleteResume(userId : int, profileId: int):
    return Resume.objects.filter(profileId=profileId, userId=userId).delete()
