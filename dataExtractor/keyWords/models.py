from django.db import models
from django.utils.timezone import now

class Keywords(models.Model):
    id = models.BigIntegerField(primary_key=True)
    resumeKeyWords = models.TextField(null=True)
    jdKeyWords = models.TextField(null=True)
    skillsPresent = models.TextField(null=True)
    skillsAbsent = models.TextField(null=True)
    uploadedDateTime = models.DateTimeField(default=now)

    def __str__(self):
        return self.id
    class Meta:
        db_table = "dataextraction_keywords"