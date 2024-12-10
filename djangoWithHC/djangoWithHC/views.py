from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello. This is the home page.")
    return render(request, "website/index.html")

def about(request):
    # return HttpResponse("Hello. This is the about page.")
    return render(request, 'website/about.html')

def contact(request):
    # return HttpResponse("Hello. This is the contact page.")
    return render(request, 'website/contact.html')

