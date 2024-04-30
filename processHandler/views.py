import datetime

from root.models import BaseRs
from root.uploadSerializer import BaseRsSerializer
from .models import Process, Resume, JobDescription
from .serializer import ExtendedProcessSerializer, JobDescriptionSerializer, ProcessSerializer, ResumeSerializer

def getProcess(id):
    process = Process.objects.get(id=id)
    serializer = ProcessSerializer(process, many=False)
    return serializer.data

def getProcessDto(id):
    return Process.objects.get(id=id)

def getProcessesByUserId(userId):
    process = Process.objects.filter(userId=userId)
    serializer = ProcessSerializer(process, many=True)
    return serializer.data

def getProcessByUserIdDto(userId):
    processes = Process.objects.filter(userId=userId)
    return processes

def getExtendedProcessesByUserId(userId):
    process = Process.objects.filter(userId=userId)
    serializer = ExtendedProcessSerializer(process, many=True)
    return serializer.data

def getJobDescription(id):
    jobDescription = JobDescription.objects.get(reqId=id)
    serializer = JobDescriptionSerializer(jobDescription, many=False)
    return serializer.data

def getJobDescriptionDto(id):
    return JobDescription.objects.get(reqId=id)

def getJobDescriptionsByUserId(userId):
    jobDescription = JobDescription.objects.filter(userId=userId)
    serializer = JobDescriptionSerializer(jobDescription, many=True)
    return serializer.data

def getJobDescriptionsByUserIdDto(userId):
    return JobDescription.objects.filter(userId=userId)

def getResume(id):
    resume = Resume.objects.get(profileId=id)
    serializer = ResumeSerializer(resume, many=False)
    return serializer.data

def getResumeDto(id):
    return Resume.objects.get(profileId=id)

def getResumesByUserId(userId):
    resume = Resume.objects.filter(userId=userId)
    serializer = ResumeSerializer(resume, many=True)
    return serializer.data

def getResumesByUserIdDto(userId):
    return Resume.objects.filter(userId=userId)

def saveProcess( userId : int, jdText : str, jdTitle: str , resumeText: str, fileName : str ):
    saveResume = Resume.objects.create(userId = userId, resumeText = resumeText, fileName= fileName ,uploadedDateTime = datetime.datetime.utcnow());
    saveJd = JobDescription.objects.create(userId = userId, jdText = jdText, jdTitle= jdTitle ,uploadedDateTime = datetime.datetime.utcnow());
    serializer = ProcessSerializer(Process.objects.create(userId = userId, reqId = saveJd.reqId, profileId= saveResume.profileId ,uploadedDateTime = datetime.datetime.utcnow()), many=False)
    return serializer.data

def saveProcessWithExistingData( userId : int, reqId : int, profileId: int ):
    serializer = ProcessSerializer(Process.objects.create(userId = userId, reqId = reqId, profileId= profileId ,uploadedDateTime = datetime.datetime.utcnow()), many=False)
    return serializer.data

def saveJobDescription( userId : int, jdText : str, jdTitle: str ):
    serializer = JobDescriptionSerializer(JobDescription.objects.create(userId = userId, jdText = jdText, jdTitle= jdTitle ,uploadedDateTime = datetime.datetime.utcnow()), many=False)
    return serializer.data;

def updateJobDescription(reqId:int, jdText : str ):
    return JobDescription.objects.filter(reqId =reqId).update(jdText = jdText ,uploadedDateTime = datetime.datetime.utcnow())

def saveResume( user, resumeText: str, profileTitle : str, fileName : str ):
    if user.role.lower() == "EMPLOYEE".lower() :
        resumes = getResumesByUserIdDto(user.id)
        profileIds = [ resume.profileId for resume in resumes ]
        updateResumeActiveFlags(profileIds,False)
    serializer = ResumeSerializer(Resume.objects.create(userId = user.id, resumeText = resumeText, profileTitle = profileTitle , fileName= fileName ,uploadedDateTime = datetime.datetime.utcnow()), many=False)
    return serializer.data;

def updateResumeActiveFlags( profileIds , flag: bool):
    Resume.objects.filter(profileId__in =profileIds).update(isActive = flag)

def updateResumeActiveFlag( user, profileId , flag: bool):
    if user.role.lower() == "EMPLOYEE".lower() :
        resumes = getResumesByUserIdDto(user.id)
        profileIds = [ resume.profileId for resume in resumes ]
        updateResumeActiveFlags(profileIds,False)    
    Resume.objects.filter(profileId = profileId).update(isActive = flag)

def deleteJobDescription(userId : int, reqId: int):
    JobDescription.objects.filter(reqId=reqId, userId=userId).delete()
    serializer = BaseRsSerializer(BaseRs(status = "200", message="success"), many=False)
    return serializer.data;

def deleteResume(userId : int, profileId: int):
    Resume.objects.filter(profileId=profileId, userId=userId).delete()
    serializer = BaseRsSerializer(BaseRs(status = "200", message="success"), many=False)
    return serializer.data;
