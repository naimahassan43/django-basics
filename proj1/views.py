from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
 data={
  'title':'Home Page',
  'bdata': 'Welcome to Django projects Home Page',
 }
 return render(request,"index.html",data)

def about(request):
 return HttpResponse("Welcome to About page.")

def course(request):
 return HttpResponse("Welcome to course page.")


def courseDetails(request,courseid):
 return HttpResponse(courseid)