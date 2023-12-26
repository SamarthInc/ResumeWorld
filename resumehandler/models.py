from django.db import models

class Resume(models.Model):
    resumeText = models.TextField()
    uploadedDateTime = models.DateTimeField()
