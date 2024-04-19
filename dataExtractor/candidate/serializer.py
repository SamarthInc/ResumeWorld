from rest_framework import serializers
from dataExtractor.candidate.models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('id', 'fullName', 'phoneNumber', 'email', 'linkedinUrl','githubUrl','uploadedDateTime')        
