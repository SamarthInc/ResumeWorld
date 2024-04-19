from django.db import models
from django.utils.timezone import now
from dataExtractor.resume.models import Resume

# Create your models here.

class Candidate(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fullName = models.TextField(null=True)
    phoneNumber =models.TextField(null=True)
    email = models.TextField(null=True)
    linkedinUrl = models.TextField(null=True)
    githubUrl = models.TextField(null=True)
    uploadedDateTime = models.DateTimeField(default=now)

    def __str__(self):
        return self.id  
    class Meta:
        db_table = "dataextraction_candidate"
