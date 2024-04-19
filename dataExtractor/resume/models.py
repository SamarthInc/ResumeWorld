from django.db import models

class Resume(models.Model):
    id = models.BigIntegerField(primary_key=True)
    text = models.TextField(null=True)
    uploadedDateTime = models.DateTimeField()

    def __str__(self):
        return self.id
    
    class Meta:
        db_table = "dataextraction_resume"