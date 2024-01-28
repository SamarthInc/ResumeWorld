from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from processHandler.utilities.ReadPdf import readPdf
from processHandler.views import getProcess, saveProcess
from .uploadSerializer import UploadSerializer
    
# ViewSets define the view behavior.
class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def getProcess(self, request):
        processId = request.query_params.get('processId')
        return Response(getProcess(processId));

    def saveProcess(self, request):
        fileUploaded = request.FILES['resume']
        content_type = fileUploaded.content_type
        if(content_type != "application/pdf"):
         response = "POST API and you have uploaded a {} file".format(content_type)
         return Response(response)
        else:
            data =readPdf(fileUploaded)
            jobDescription = request.data['jobDescription']
            process = saveProcess(data, jobDescription)
            return Response(process.id)   