from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello. This is the home page.")

def about(request):
    return HttpResponse("Hello. This is the about page.")

def contact(request):
    return HttpResponse("Hello. This is the contact page.")

