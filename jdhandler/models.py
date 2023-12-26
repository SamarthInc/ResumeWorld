import datetime
from django.db import models

# Create your models here.
from django.db import models
class JobDecription(models.Model):
    id = models.AutoField (primary_key=True),
    jdText = models.TextField()
    uploadedDateTime = models.DateTimeField(default=datetime.datetime.utcnow(), blank=False)
