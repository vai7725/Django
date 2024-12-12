from django.shortcuts import render

# Create your views here.
def all(request):
    return render(request, 'newApp/all.html')