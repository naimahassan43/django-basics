from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
 # data={
 #  'title':'Home Page',
 #  'bdata': 'Welcome to Django projects Home Page',
 #  'clist': ['php', 'python', 'django'],
 #  'numbers': ['15', '24', '34','45'],
 #  'student_details':[
 #   {'name': 'Naima', 'phone': '07405084878'},
 #   {'name': 'Rahdi', 'phone': '07405084800'},
 #  ]
 # }
 return render(request,"index.html")

def businessRate(request):
 return render(request,"business-rate.html")

def services(request):
 return render(request,"services.html")

def userForm(request):
 final = 0
 try:
  # n1 = int(request.GET['val1'])
  # n2 = int(request.GET['val2'])
  n1 = int(request.GET.get('val1'))
  n2 = int(request.GET.get('val2'))
  final = n1+n2
 except:
   pass
 return render(request,"userform.html", {'output': final})
