from django.urls import path, include
from .views import PercentageMatch,UploadViewSet
#from .comparision.storing import ResumeJobStoring

urlpatterns = [
    #path('PercentageMatch',PercentageMatch.as_view()),
    #path('ResumeJobStoring',ResumeJobStoring.as_view()),
    path('getJd', UploadViewSet.as_view({'get': 'getResume'})),
    path('getResume', UploadViewSet.as_view({'get': 'getResume'})),
    path('upload', UploadViewSet.as_view({'post': 'create'})),
]
