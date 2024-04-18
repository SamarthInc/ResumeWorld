from django.urls import path, include
from .views import UploadViewSet
#from .comparision.storing import ResumeJobStoring

urlpatterns = [
    path('getProcess', UploadViewSet.as_view({'get': 'getProcess'})),
    path('getProcessesByUserId', UploadViewSet.as_view({'get': 'getProcessesByUserId'})),
    path('getResumesByUserId', UploadViewSet.as_view({'get': 'getResumesByUserId'})),
    path('getJobDescriptionsByUserId', UploadViewSet.as_view({'get': 'getJobDescriptionsByUserId'})),
    path('saveProcess', UploadViewSet.as_view({'post': 'saveProcess'})),
    path('saveProcessWithExistingData', UploadViewSet.as_view({'post': 'saveProcessWithExistingData'})),
    path('saveJobDescription', UploadViewSet.as_view({'post': 'saveJobDescription'})),
    path('saveResume', UploadViewSet.as_view({'post': 'saveResume'})),
    path('getReport', UploadViewSet.as_view({'get': 'getReport'})),
    path('deleteJobDescription', UploadViewSet.as_view({'delete': 'deleteJobDescription'})),
    path('deleteResume', UploadViewSet.as_view({'delete': 'deleteResume'})),
    path('auth/',include('users.urls')),
]

