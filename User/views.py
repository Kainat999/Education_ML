from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserRegistrationSerializer, UserProfileSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


@api_view(['POST'])
def user_registration(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def user_login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

from rest_framework_simplejwt.tokens import BlacklistedToken

@api_view(['POST'])
def user_logout(request):
    refresh_token = request.data["refresh"]
    token = RefreshToken(refresh_token)
    token.blacklist()

    return Response(status=status.HTTP_205_RESET_CONTENT)




@api_view(['GET', 'PUT'])
def user_profile(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




 
def home(request):
    return render(request, 'home.html')

def register_view(request):
    return render(request, 'register.html')



def login_view(request):
    return render(request, 'login.html')

@login_required
def profile_view(request):
    if request.user.is_authenticated:  # This check is somewhat redundant due to the @login_required decorator, but can be kept for clarity
        try:
            userprofile = UserProfile.objects.get(user=request.user)
            return render(request, 'profile.html', {'userprofile': userprofile})
        except UserProfile.DoesNotExist:
            # Handle this case if the profile doesn't exist
            return HttpResponseForbidden("Profile not found.")
    else:
        return HttpResponseForbidden("You need to be logged in to view the profile.")
