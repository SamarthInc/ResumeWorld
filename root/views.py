from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from processHandler.utilities.ReadPdf import readPdf
from processHandler.utilities.ReadDoc import readDoc
from processHandler.views import getProcessDto, deleteJobDescription, deleteResume, getExtendedProcessesByUserId, getJobDescriptionDto, getProcess, getResumeDto, saveProcess, saveProcessWithExistingData, getResumesByUserId, getJobDescriptionsByUserId, saveJobDescription, saveResume
from reportExtractor.views import defaultScoreConfigDataDto, saveScoreConfigData, scoreConfigData, scoreData
from .uploadSerializer import UploadSerializer
from root.analyse import *
from rest_framework.permissions import IsAuthenticated
    
# ViewSets define the view behavior.
class UploadViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UploadSerializer

    def getProcess(self, request):
        processId = request.query_params.get('processId')
        return Response(getProcess(processId));

    def getProcessesByUserId(self, request):
        return Response(getExtendedProcessesByUserId(request.user.id));

    def getResumesByUserId(self, request):
        return Response(getResumesByUserId(request.user.id));

    def getJobDescriptionsByUserId(self, request):
        return Response(getJobDescriptionsByUserId(request.user.id));

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
            process = saveProcess(request.user.id, request.data['jobDescription'], request.data['jobDescriptionTitle'],data, fileUploaded.name)
            return Response(process.id)     
        else:
            response = "POST API and you have uploaded a {} file".format(content_type)
            return Response(response)
    def saveProcessWithExistingData(self, request):
        resume = None 
        jd = None 
        try :
            resume = getResumeDto(request.data['profileId'])
        except:
            resume = None  
        try :
            jd = getJobDescriptionDto(request.data['reqId'])
        except :
            jd = None 
        if jd is None or resume is None :
            return Response("process or resume doesnt exist", status=400)
        if jd.userId != request.user.id or resume.userId != request.user.id :
            return Response("process or resume doesnt map to userId", status=400)
        process = saveProcessWithExistingData(request.user.id, request.data['reqId'] , request.data['profileId'])
        return Response(process.id)  

    def saveJobDescription(self, request):
        process = saveJobDescription(request.user.id, request.data['jdText'] , request.data['jdTitle'])
        defaultConfig = defaultScoreConfigDataDto(1)
        keywordsConfig = request.POST.get('keywordsConfig', defaultConfig.keywordsConfig)
        experienceConfig = request.POST.get('experienceConfig', defaultConfig.experienceConfig)
        educationConfig = request.POST.get('educationConfig', defaultConfig.educationConfig)
        saveScoreConfigData(process.reqId, keywordsConfig, experienceConfig, educationConfig)
        return Response(process.reqId) 

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
            process = saveResume(request.user.id, data, profileTitle, fileUploaded.name)
            return Response(process.profileId)    
        else:
            response = "POST API and you have uploaded a {} file".format(content_type)
            return Response(response)    
        
    def getReport(self,request):
        processId = request.query_params.get('processId')
        return Response(scoreData(processId))   
    
    def deleteJobDescription(self,request):
        return Response(deleteJobDescription(request.user.id,request.query_params.get('reqId')))
    
    def deleteResume(self,request):
        return Response(deleteResume(request.user.id,request.query_params.get('profileId')))
    
    def ProcessResume(self, request):
        print(request.user.id)
        processId = request.data["processId"]
        processId = int(processId)
        process = getProcessDto(processId)
        resumeText = getResumeDto(process.profileId).resumeText
        jdText = getJobDescriptionDto(process.reqId).jdText
        print(resumeText)
        extractAndSaveData(process.id, process.reqId, resumeText, jdText)
        return Response("success")

    def getCleanResume(self,request):
        processId = request.query_params.get('processId')
        return Response(getResume(processId))
    
    def getCleanJobDescription(self,request):
        processId = request.query_params.get('processId')
        return Response(getJd(processId))

    def getCandidate(self,request):
        processId = request.query_params.get('processId')
        return Response(getProfile(processId))

    def getEducation(self,request):
        processId = request.query_params.get('processId')
        return Response(getEducation(processId))

    def getExperience(self,request):
        processId = request.query_params.get('processId')
        return Response(getExperience(processId))
    
    def getKeywords(self,request):
        processId = request.query_params.get('processId')
        return Response(getKeywords(processId))
    
    def getReport(self,request):
        processId = request.query_params.get('processId')
        return Response(getReport(processId))
    
    def getReportConfig(self,request):
        configId = request.query_params.get('configId')
        return Response(getReportConfig(configId))