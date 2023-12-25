from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
# Create your views here.

class Test(APIView):
    def post(self,request):

        return Response("success")



class PercentageMatch(APIView):
    def post(self,request):
        job_description = request.data['job_description']
        resume = request.data['resume']
        resume_script=''.join(resume)
        resume_Clear = resume_script.replace("\n","")
        job_description_script=''.join(job_description)
        job_description_Clear = job_description_script.replace("\n","")
        
        Match_Test=[resume_Clear,job_description_Clear]
        from sklearn.feature_extraction.text import CountVectorizer
        cv=CountVectorizer()
        count_matrix=cv.fit_transform(Match_Test)
        from sklearn.metrics.pairwise import cosine_similarity
        print('Similarity is :',cosine_similarity(count_matrix))
        MatchPercentage=cosine_similarity(count_matrix)[0][1]*100
        MatchPercentage=round(MatchPercentage,2)
        print('Match Percentage is :'+ str(MatchPercentage)+'% to Requirement')
        return JsonResponse({"matching_percentage":MatchPercentage}, status=200)