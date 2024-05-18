from django.core.mail import send_mail
from resumeWorld import settings

def logEmail(emailId : str,message: str,name : str):
    subject='Email from : '+ name
    emailList = []
    emailList.append(settings.EMAIL_HOST_USER)
    emailList.append(emailId)
    message = 'Email Id : ' + emailId + '\n' +message
    send_mail(subject,message,settings.EMAIL_HOST_USER,emailList,fail_silently=False)    
