from django.db import models

class JobDescription(models.Model):
    reqId = models.AutoField (primary_key=True)
    userId = models.BigIntegerField(null=True)
    jdText = models.TextField()
    jdTitle = models.TextField(null=True, unique=True)
    uploadedDateTime = models.DateTimeField()

    class Meta:
        unique_together = 'userId', 'jdTitle'   

    def __str__(self):
        return self.reqId  
    
class Resume(models.Model):
    profileId = models.AutoField (primary_key=True)
    userId = models.BigIntegerField(null=True)
    resumeText = models.TextField()
    profileTitle = models.TextField(null=True)
    fileName = models.TextField()
    uploadedDateTime = models.DateTimeField()

    class Meta:
      unique_together = 'userId', 'profileTitle'

    def __str__(self):
        return self.profileId


class Process(models.Model):
    id = models.AutoField (primary_key=True)
    userId = models.BigIntegerField(null=True)
    reqId = models.BigIntegerField(null=True)
    profileId = models.BigIntegerField(null=True)
    uploadedDateTime = models.DateTimeField()

    def __str__(self):
        return self.id  
