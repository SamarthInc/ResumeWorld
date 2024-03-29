from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from processHandler.utilities.ReadPdf import readPdf
from processHandler.utilities.ReadDoc import readDoc
from processHandler.views import getExtendedProcessesByUserId, getProcess, saveProcess, saveProcessWithExistingData, getResumesByUserId, getJobDescriptionsByUserId, saveJobDescription, saveResume
from reportExtractor.views import scoreData
from .uploadSerializer import UploadSerializer
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
        process = saveProcessWithExistingData(request.user.id, request.data['reqId'] , request.data['profileId'])
        return Response(process.id)  

    def saveJobDescription(self, request):
        process = saveJobDescription(request.user.id, request.data['jdText'] , request.data['jdTitle'])
        return Response(process.reqId) 

    def saveResume(self, request):
        fileUploaded = request.FILES['resume']
        content_type = fileUploaded.content_type
        checkfile = fileUploaded.name.split(".")
        print(checkfile)
        if str(checkfile[1]) == "docx" or str(checkfile[1]) == "pdf":
            if str(checkfile[1]) == "pdf":
                data =readPdf(fileUploaded)
            if str(checkfile[1]) == "docx":
                data =readDoc(fileUploaded)
            process = saveResume(request.user.id, data, fileUploaded.name)
            return Response(process.profileId)    
        else:
            response = "POST API and you have uploaded a {} file".format(content_type)
            return Response(response)    
        
    def getReport(self,request):
        processId = request.query_params.get('processId')
        return Response(scoreData(processId))   