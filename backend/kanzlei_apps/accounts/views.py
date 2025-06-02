#from django.shortcuts import render

# Create your views here.
# backend/kanzlei_apps/accounts/views.py
from django.http import HttpResponse

def profile_view(request):
    return HttpResponse("Profilseite")