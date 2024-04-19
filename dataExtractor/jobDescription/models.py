from django.db import models

# Create your models here.
class JobDescription(models.Model):
    id = models.BigIntegerField(primary_key=True)
    text = models.TextField()
    uploadedDateTime = models.DateTimeField(null=True)

    def __str__(self):
        return self.id

    class Meta:
        db_table = "dataextraction_jobdescription"
