from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
 data={
  'title':'Home Page',
  'bdata': 'Welcome to Django projects Home Page',
  'clist': ['php', 'python', 'django'],
  'student_details':[
   {'name': 'Naima', 'phone': '07405084878'},
   {'name': 'Rahdi', 'phone': '07405084800'},
  ]
 }
 return render(request,"index.html",data)

def about(request):
 return HttpResponse("Welcome to About page.")

def course(request):
 return HttpResponse("Welcome to course page.")


def courseDetails(request,courseid):
 return HttpResponse(courseid)