from django.db import models
from django.utils.timezone import now

class Education(models.Model):
    id = models.BigIntegerField(primary_key=True)
    text = models.TextField(null=True)
    uploadedDateTime = models.DateTimeField(default=now)

    def __str__(self):
        return self.id
    
    class Meta:
        db_table = "dataextraction_education"
