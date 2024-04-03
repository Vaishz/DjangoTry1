from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, "home.html")

def reviews(request):
    return render(request, "reviews.html")

def project(request):
    return render(request, "project.html")

def vaish(request):
    return render(request, "vaish.html")

def kinda(request):
    return render(request, "kindarunning.html")
