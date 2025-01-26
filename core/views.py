from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.oauth2.views import OAuth2LoginView

# Create your views here.

def login(request):
    return render(request, 'account/login.html')

@login_required
def profile(request):
    return render(request, 'account/profile.html')
