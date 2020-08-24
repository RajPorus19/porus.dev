from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def other(request):
    return render(request, 'home/other.html')