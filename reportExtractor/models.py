from django.db import models
from django.utils.timezone import now

class Score(models.Model):
    id = models.BigIntegerField(primary_key=True)
    configId =models.BigIntegerField(null = False)
    keywordsScore = models.FloatField(null=True)
    experienceScore = models.FloatField(null=True)
    educationScore=models.FloatField(null=True)
    finalScore=models.FloatField(null=True)
    uploadedDateTime = models.DateTimeField(default=now)

    def __str__(self):
        return self.id
    class Meta:
        db_table = "score"


class ScoreConfig(models.Model):
    jobId = models.BigIntegerField(primary_key=True)
    keywordsConfig = models.IntegerField(null=True)
    experienceConfig = models.IntegerField(null=True)
    educationConfig=models.IntegerField(null=True)
    uploadedDateTime = models.DateTimeField(default=now)

    def __str__(self):
        return self.jobId
    class Meta:
        db_table = "score_config"

class DefaultScoreConfig(models.Model):
    id = models.BigIntegerField(primary_key=True)
    keywordsConfig = models.IntegerField(null=True)
    experienceConfig = models.IntegerField(null=True)
    educationConfig=models.IntegerField(null=True)
    uploadedDateTime = models.DateTimeField(default=now)

    def __str__(self):
        return self.id
    class Meta:
        db_table = "default_score_config"        