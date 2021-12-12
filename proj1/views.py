from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
 return render(request,"index.html")

def about(request):
 return HttpResponse("Welcome to About page.")

def course(request):
 return HttpResponse("Welcome to course page.")


def courseDetails(request,courseid):
 return HttpResponse(courseid)