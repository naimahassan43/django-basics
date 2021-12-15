from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import usersForm

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
 if request.method=="GET":
  output = request.GET.get('output')
 return render(request,"services.html", {'output': output})

def calculatorForm(request):
  c = ''
  try:
    if request.method=="POST":
      n1       = eval(request.POST.get('val1'))
      n2       = eval(request.POST.get('val2'))
      operator = request.POST.get('operator')
      if operator == '+':
        c = n1+n2
      elif operator == '-':
        c = n1-n2
      elif operator == '*':
        c = n1*n2
      elif operator == '/':
        c = n1/n2
      
  except:
    c = "Invalid operator..."
    print(c)

  return render(request,"calculator.html", {'c':c})
def evenodd(request):
  c = ''
  if request.method == "POST":
    n = eval(request.POST.get('val'))
    if n % 2 == 0:
      c = "Even Number"
    else:
      c = "Odd Number"

  return render(request,"evenodd.html", {'c':c})

def userForm(request):
 final = 0
 fn = usersForm()

 data={'form':fn}
 try:
  if request.method == "POST":
  # n1 = int(request.GET['val1'])
  # n2 = int(request.GET['val2'])
   n1 = int(request.POST.get('val1'))
   n2 = int(request.POST.get('val2'))
   final = n1+n2
   data = {
    'form':fn,
    'output': final
    }
   url = "/services/?output={}".format(final)
   return HttpResponseRedirect(url)
 except:
   pass
 return render(request,"userform.html", data)

 

# def submitForm(request):
#   try:
#     if request.method == 'POST':
#       n1 = int(request.POST.get('num1'))
#       n2 = int(request.POST.get('num2'))
#       final = n1 + n2
#       data = {
#         'n1':n1,
#         'n2':n2,
#         'output': final
#         }
      
#     return HttpResponse(final)
#   except:
#     pass


  

   
