from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from processHandler.utilities.ReadPdf import readPdf
from processHandler.utilities.ReadDoc import readDoc
from processHandler.views import getProcessByUserIdDto, getProcessDto, deleteJobDescription, deleteResume, getExtendedProcessesByUserId, getJobDescriptionDto, getProcess, getProcessesByUserId, getResumeDto, saveProcess, saveProcessWithExistingData, getResumesByUserId, getJobDescriptionsByUserId, saveJobDescription, saveResume, updateJobDescription, updateResumeActiveFlag
from reportExtractor.views import defaultScoreConfigDataDto, saveScoreConfigData, scoreConfigData, scoreData
from root.models import BaseRs, RootException
from users.models import EmailUpload
from users.serializer import EmailSerializer
from .uploadSerializer import BaseRsSerializer, ExtendedReportSerializer, LimitedExtendedReportSerializer, UploadSerializer
from root.analyse import *
from root.admin import EmailUploadFilter,saveEmail_and_Send
from rest_framework.permissions import IsAuthenticated
    
# ViewSets define the view behavior.
class UploadViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UploadSerializer

    def validateProcess(self,processId, userId):
        process = getProcessDto(processId)
        if process.userId != userId :
            raise RootException(detail="user is not associated to process")   
        
    def getProcess(self, request):
        processId = request.query_params.get('processId')
        return Response(getProcess(processId));

    def getProcessesByUserId(self, request):
        return Response(getProcessesByUserId(request.user.id));

    def getExtendedProcessesByUserId(self, request):
        return Response(getExtendedProcessesByUserId(request.user.id));

    def getResumesByUserId(self, request):
        return Response(getResumesByUserId(request.user.id));

    def getJobDescriptionsByUserId(self, request):
        return Response(getJobDescriptionsByUserId(request.user.id));

    def updateJobDescription(self, request) :
        userJds= getJobDescriptionsByUserId(request.user.id)
        for resume in userJds :
            if resume['reqId'] == request.data['reqId'] :
                return Response(updateJobDescription(request.data['reqId'], request.data['jdText']));
        raise RootException(detail="user is not associated to job description")          

    def saveProcess(self, request):
        fileUploaded = request.FILES['resume']
        content_type = fileUploaded.content_type
        checkfile = fileUploaded.name.split(".")
        print(checkfile)
        if str(checkfile[1]) == "docx" or str(checkfile[1]) == "pdf":
            if str(checkfile[1]) == "pdf":
                data =readPdf(fileUploaded)
            if str(checkfile[1]) == "docx":
                data =readDoc(fileUploaded)
            return Response(saveProcess(request.user.id, request.data['jobDescription'], request.data['jobDescriptionTitle'],data, fileUploaded.name))    
        else:
            raise RootException(detail="POST API and you have uploaded a {} file".format(content_type))

    def saveProcessWithExistingData(self, request):
        print(request.data['profileId'])
        resume = getResumeDto(request.data['profileId'])
        print(resume)
        if resume.isActive == False :
            raise RootException(detail="resume is inactive")
        jd = getJobDescriptionDto(request.data['reqId'])
        if jd is None or resume is None :
            raise RootException(detail="process or resume doesnt exist")
        if jd.userId != request.user.id or resume.userId != request.user.id :
            raise RootException(detail="process or resume doesnt map to userId")
        return Response(saveProcessWithExistingData(request.user.id, request.data['reqId'] , request.data['profileId']))

    def saveJobDescription(self, request):
        process = saveJobDescription(request.user.id, request.data['jdText'] , request.data['jdTitle'])
        defaultConfig = defaultScoreConfigDataDto(1)
        keywordsConfig = request.POST.get('keywordsConfig', defaultConfig.keywordsConfig)
        experienceConfig = request.POST.get('experienceConfig', defaultConfig.experienceConfig)
        educationConfig = request.POST.get('educationConfig', defaultConfig.educationConfig)
        saveScoreConfigData(process['reqId'], keywordsConfig, experienceConfig, educationConfig)
        return Response(process) 

    def saveResume(self, request):
        fileUploaded = request.FILES['resume']
        profileTitle = request.data['profileTitle']
        content_type = fileUploaded.content_type
        checkfile = fileUploaded.name.split(".")
        print(checkfile)
        if str(checkfile[1]) == "docx" or str(checkfile[1]) == "pdf":
            if str(checkfile[1]) == "pdf":
                data =readPdf(fileUploaded)
            if str(checkfile[1]) == "docx":
                data =readDoc(fileUploaded)
            process = saveResume(request.user, data, profileTitle, fileUploaded.name)
            return Response(process)    
        else:
            raise RootException(detail="POST API and you have uploaded a {} file".format(content_type))
        
    def updateResumeActiveFlag(self,request):
        resume = None 
        try :
            resume = getResumeDto(request.data['profileId'])
        except:
            resume = None  
        if resume.userId != request.user.id :
            raise RootException(detail="resume doesnt map to userId")
        updateResumeActiveFlag(request.user, request.data['profileId'], request.data['isActive'])
        return Response(BaseRsSerializer(BaseRs(status = "200", message= "success"), many=False).data)  
     
    def getReport(self,request):
        processId = request.query_params.get('processId')
        return Response(scoreData(processId))   
    
    def deleteJobDescription(self,request):
        return Response(deleteJobDescription(request.user.id,request.query_params.get('reqId')))
    
    def deleteResume(self,request):
        return Response(deleteResume(request.user.id,request.query_params.get('profileId')))
    
    def ProcessResume(self, request):
        processId = request.data["processId"]
        processId = int(processId)
        process = getProcessDto(processId)
        resumeText = getResumeDto(process.profileId).resumeText
        jdText = getJobDescriptionDto(process.reqId).jdText
        print(resumeText)
        extractAndSaveData(process.id, process.reqId, resumeText, jdText)
        return Response(BaseRsSerializer(BaseRs(status = "200", message= "success"), many=False).data)  

    def getCleanResume(self,request):
        processId = request.query_params.get('processId')
        self.validateProcess(processId, request.user.id)
        return Response(getResume(processId))
    
    def getCleanJobDescription(self,request):
        processId = request.query_params.get('processId')
        self.validateProcess(processId, request.user.id)        
        return Response(getJd(processId))

    def getCandidate(self,request):
        processId = request.query_params.get('processId')
        self.validateProcess(processId, request.user.id)
        return Response(getProfile(processId))

    def getEducation(self,request):
        processId = request.query_params.get('processId')
        self.validateProcess(processId, request.user.id)
        return Response(getEducation(processId))

    def getExperience(self,request):
        processId = request.query_params.get('processId')
        self.validateProcess(processId, request.user.id)
        return Response(getExperience(processId))
    
    def getKeywords(self,request):
        processId = request.query_params.get('processId')
        self.validateProcess(processId, request.user.id)
        return Response(getKeywords(processId))
    
    def getReport(self,request):
        processId = request.query_params.get('processId')
        self.validateProcess(processId, request.user.id)
        return Response(getReport(processId))
    
    def getExtendedReport(self,request):
        processId = request.query_params.get('processId')
        self.validateProcess(processId, request.user.id)
        process = getProcessDto(processId)
        serializer = ExtendedReportSerializer(process, many=False)
        return Response(serializer.data)
    
    def getReports(self,request):
        processes = getProcessByUserIdDto(request.user.id)
        reports =[]
        for process in processes:
            reports.append(LimitedExtendedReportSerializer(process).data) 
        return Response(reports)
    
    def getReportConfig(self,request):
        configId = request.query_params.get('configId')
        return Response(getReportConfig(configId)) 
    
    def contactUs(self,request):
        emailId=request.data['emailId']
        message=request.data['message']
        
        filter=EmailUploadFilter(emailId,message)
        if not filter:
            saveEmail_and_Send(emailId,message) 
        # create a model with emailID and message and sent options if sent is False(Default) then send it else block it
            return Response('Email Sent')
        else:
            return Response('Email Sent')
        
        
            
