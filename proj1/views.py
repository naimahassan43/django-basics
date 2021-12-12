from django.http import HttpResponse

def about(request):
 return HttpResponse("Welcome to About page.")

def course(request):
 return HttpResponse("Welcome to course page.")


def courseDetails(request,courseid):
 return HttpResponse(courseid)