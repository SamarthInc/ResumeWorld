from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser

from users.serializer import UserProfileSerializer
from .models import UserProfile

class RegisterUserView(APIView):
    parser_classes = [JSONParser, MultiPartParser, FormParser]
    def post(self, request):
        try:
            if UserProfile.objects.filter(email=request.data['email']).exists():
                return Response({'error': 'Email already registered'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer = UserProfileSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print( e)
    

class UserView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def get(self, request):
        serializer = UserProfileSerializer(request.user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # update user profile image
    def put(self, request):
        user = UserProfile.objects.get(email=request.user.email)
        user.avatar = request.data['avatar']
        user.save()
        return Response({'message': 'Image updated'}, status=status.HTTP_200_OK) 
