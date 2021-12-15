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
# Services
def services(request):
 if request.method=="GET":
  output = request.GET.get('output')
 return render(request,"services.html", {'output': output})

# marksheet
def marksheet(request):
  if request.method=="POST":
    s1 = eval(request.POST.get('sub1'))
    s2 = eval(request.POST.get('sub2'))
    s3 = eval(request.POST.get('sub3'))
    s4 = eval(request.POST.get('sub4'))
    total = s1+s2+s3+s4
    percentage = total*100/400
    if percentage > 60:
      d = "First Class"
    elif percentage > 50:
      d = "Second Class"
    elif percentage > 35:
      d = "Third Class"
    else:
      d = "Fail"
    data = {
      'total': total,
      'percentage': percentage,
      'div': d,
    }
    return render(request,"marksheet.html", data)
  return render(request,"marksheet.html")

# calculator
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
  # evenodd
def evenodd(request):
  c = ''
  if request.method == "POST":
    if request.POST.get('val') == "":
      return render(request,"evenodd.html", {'error':True})
    n = eval(request.POST.get('val'))
    if n % 2 == 0:
      c = "Even Number"
    else:
      c = "Odd Number"

  return render(request,"evenodd.html", {'c':c})
# userForm
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


  

   
