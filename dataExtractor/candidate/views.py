import datetime
from dataExtractor.candidate.models  import Candidate
from dataExtractor.candidate.serializer import CandidateSerializer

def candidateData(id):
    profile = Candidate.objects.get(id=id)
    serializer = CandidateSerializer(profile, many=False)
    return serializer.data

def candidateDataDto(id):
    return Candidate.objects.get(id=id)

def saveCandidateData(profile : Candidate):
    Candidate.objects.update_or_create(id = profile.id ,
                                       defaults ={
                                           'fullName' : profile.fullName ,
                                            'phoneNumber' : profile.phoneNumber ,
                                            'email' : profile.email ,
                                            'linkedinUrl' : profile.linkedinUrl ,
                                            'githubUrl' : profile.githubUrl,
                                            'uploadedDateTime' : datetime.datetime.utcnow()
                                            })
