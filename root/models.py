from django.db import models
from rest_framework import exceptions

class UploadRq(models.Model):
    resume = models.FileField()
    jobDescription = models.TextField()


class BaseRs(models.Model):
    status = models.TextField()
    message = models.TextField()

class RootException(exceptions.APIException):
    status_code = 400
    default_detail = 'An error occurred'
    default_code = 'error'
