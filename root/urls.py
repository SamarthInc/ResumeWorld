from django.urls import path, include
from .views import UploadViewSet
#from .comparision.storing import ResumeJobStoring

urlpatterns = [
    path('getProcess', UploadViewSet.as_view({'get': 'getProcess'})),
    path('saveProcess', UploadViewSet.as_view({'post': 'saveProcess'}))
]

