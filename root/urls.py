from django.urls import path, include
from .views import UploadViewSet
#from .comparision.storing import ResumeJobStoring

urlpatterns = [
    path('auth/',include('users.urls')),
    path('getProcess', UploadViewSet.as_view({'get': 'getProcess'})),
    path('getExtendedProcessesByUserId', UploadViewSet.as_view({'get': 'getExtendedProcessesByUserId'})),
    path('getProcessesByUserId', UploadViewSet.as_view({'get': 'getProcessesByUserId'})),
    path('getResumesByUserId', UploadViewSet.as_view({'get': 'getResumesByUserId'})),
    path('getJobDescriptionsByUserId', UploadViewSet.as_view({'get': 'getJobDescriptionsByUserId'})),
    path('saveProcess', UploadViewSet.as_view({'post': 'saveProcess'})),
    path('saveProcessWithExistingData', UploadViewSet.as_view({'post': 'saveProcessWithExistingData'})),
    path('saveJobDescription', UploadViewSet.as_view({'post': 'saveJobDescription'})),
    path('saveResume', UploadViewSet.as_view({'post': 'saveResume'})),
    path('updateResumeActiveFlag', UploadViewSet.as_view({'post': 'updateResumeActiveFlag'})),
    path('getReport', UploadViewSet.as_view({'get': 'getReport'})),
    path('deleteJobDescription', UploadViewSet.as_view({'delete': 'deleteJobDescription'})),
    path('deleteResume', UploadViewSet.as_view({'delete': 'deleteResume'})),
    path('processResume', UploadViewSet.as_view({'post': 'ProcessResume'})),
    path('getCleanResume', UploadViewSet.as_view({'get': 'GetCleanResume'})),
    path('getCleanJobDescription', UploadViewSet.as_view({'get': 'GetCleanJobDescription'})),
    path('getCandidate', UploadViewSet.as_view({'get': 'getCandidate'})),
    path('getEducation', UploadViewSet.as_view({'get': 'getEducation'})),
    path('getExperience', UploadViewSet.as_view({'get': 'getExperience'})),
    path('getExtendedReport', UploadViewSet.as_view({'get': 'getExtendedReport'})),
    path('getReport', UploadViewSet.as_view({'get': 'getReport'})),
    path('getReports', UploadViewSet.as_view({'get': 'getReports'})),
    path('getReportConfig', UploadViewSet.as_view({'get': 'getReportConfig'})),
    path('getKeywords', UploadViewSet.as_view({'get': 'getKeywords'}))
]

