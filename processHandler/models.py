from django.db import models

class Process(models.Model):
    id = models.AutoField (primary_key=True)
    resumeText = models.TextField()
    jdText = models.TextField()
    uploadedDateTime = models.DateTimeField()

    def __str__(self):
        return self.id  
