from rest_framework import serializers
from processHandler.models import JobDescription, Process, Resume
from processHandler.serializer import JobDescriptionSerializer, ResumeSerializer
from root.analyse import getEducation, getExperience, getExtendedReport, getKeywords, getProfile
from root.models import BaseRs, UploadRq


class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadRq
        fields = ('resume', 'jobDescription')

class BaseRsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseRs
        fields = ('status', 'message')



class ExtendedReportSerializer(serializers.ModelSerializer):
    resume = serializers.SerializerMethodField()
    jobDescription = serializers.SerializerMethodField()
    scoreDetails = serializers.SerializerMethodField()
    candidateDetails = serializers.SerializerMethodField()
    experience = serializers.SerializerMethodField()
    education = serializers.SerializerMethodField()
    keyWords = serializers.SerializerMethodField()

    class Meta:
        model = Process
        fields = ('id', 'userId', 'reqId', 'profileId', 'uploadedDateTime', 
                  'resume', 'jobDescription','scoreDetails','candidateDetails','experience', 'education', 'keyWords')   

    def get_resume(self, obj):
        resume = Resume.objects.filter(profileId=obj.profileId)
        return ResumeSerializer(resume, many=True).data  

    def get_jobDescription(self, obj):
        jobDescription = JobDescription.objects.filter(reqId=obj.reqId)
        return JobDescriptionSerializer(jobDescription, many=True).data   

    def get_scoreDetails(self, obj):
        try :
         return getExtendedReport(obj.id)
        except:
            return None
    
    def get_experience(self, obj):
        try :
            return getExperience(obj.id)   
        except:
            return None  
    
    def get_education(self, obj):
        try :
            return getEducation(obj.id) 
        except:
            return None  
    
    def get_keyWords(self, obj):
        try :
            return getKeywords(obj.id)   
        except:
            return None  
    
    def get_candidateDetails(self, obj):
        try :
            return getProfile(obj.id)    
        except:
            return None     




class LimitedExtendedReportSerializer(serializers.ModelSerializer):
    resume = serializers.SerializerMethodField()
    jobDescription = serializers.SerializerMethodField()
    scoreDetails = serializers.SerializerMethodField()

    class Meta:
        model = Process
        fields = ('id', 'userId', 'reqId', 'profileId', 'uploadedDateTime', 
                  'resume','jobDescription', 'scoreDetails')   

    def get_resume(self, obj):
        resume = Resume.objects.filter(profileId=obj.profileId).get()
        return {'profileId' :resume.profileId , 'profileTitle': resume.profileTitle}

    def get_jobDescription(self, obj):
        jobDescription = JobDescription.objects.filter(reqId=obj.reqId).get()
        return {'reqId' :jobDescription.reqId , 'jdTitle': jobDescription.jdTitle} 

    def get_scoreDetails(self, obj):
        try :
         return getExtendedReport(obj.id)
        except:
            return None         