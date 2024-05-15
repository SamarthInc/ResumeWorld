#from django.contrib import admin
from users.models import EmailUpload
from users.serializer import EmailSerializer
from django.core.mail import send_mail
from resumeWorld import settings
# Register your models here.

def getEmailUpload(email,message):
    emailUpload= EmailUpload.objects.get(emailId=email,message=message)
    serializer=EmailSerializer(emailUpload,many=False)
    return serializer.data

def EmailUploadFilter(email,message):
    emailUpload=EmailUpload.objects.filter(emailId=email,message=message)
    return emailUpload

def saveEmail_and_Send(email : str,message: str):
    EmailUpload.objects.create(emailId=email,message=message)
    message=email+2*'\n'+message
    send_mail("Contact through SampleFE",message,settings.EMAIL_HOST_USER,['nikhileswar.mada@myamico.net'],fail_silently=False)    
