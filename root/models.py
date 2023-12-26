from django.db import models

class UploadRq(models.Model):
    resume = models.FileField()
    jobDescription = models.TextField()
