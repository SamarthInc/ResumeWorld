from rest_framework import serializers
from processHandler. models import Process, Resume, JobDescription


class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = ('id', 'userId', 'reqId', 'profileId', 'uploadedDateTime')

class JobDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDescription
        fields = ('reqId', 'userId', 'jdText', 'jdTitle','uploadedDateTime')       

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ('profileId', 'userId', 'resumeText', 'profileTitle', 'isActive', 'fileName','uploadedDateTime')


class ExtendedProcessSerializer(serializers.ModelSerializer):
    resume = serializers.SerializerMethodField()
    jobDescription = serializers.SerializerMethodField()
    class Meta:
        model = Process
        fields = ('id', 'userId', 'reqId', 'profileId', 'uploadedDateTime','resume', 'jobDescription')        

    def get_resume(self, obj):
        resume = Resume.objects.filter(profileId=obj.profileId)
        return ResumeSerializer(resume, many=True).data  

    def get_jobDescription(self, obj):
        jobDescription = JobDescription.objects.filter(reqId=obj.reqId)
        return JobDescriptionSerializer(jobDescription, many=True).data        
