from django.urls import path,include
from django.conf.urls import url
from .views import Test,PercentageMatch
from .comparision.storing import ResumeJobStoring
urlpatterns = [
    url('test',Test.as_view()),
    url('PercentageMatch',PercentageMatch.as_view()),
    url('ResumeJobStoring',ResumeJobStoring.as_view()),
    
]
