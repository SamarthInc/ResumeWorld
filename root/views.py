from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from processHandler.utilities.ReadPdf import readPdf
from processHandler.utilities.ReadDoc import readDoc
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
        checkfile = fileUploaded.name.split(".")
        print(checkfile)
        if str(checkfile[1]) == "docx" or str(checkfile[1]) == "pdf":
            if str(checkfile[1]) == "pdf":
                data =readPdf(fileUploaded)
            if str(checkfile[1]) == "docx":
                data =readDoc(fileUploaded)
            jobDescription = request.data['jobDescription']
            process = saveProcess(data, jobDescription)
            return Response(process.id)     
        else:
            response = "POST API and you have uploaded a {} file".format(content_type)
            return Response(response)