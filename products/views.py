from django.shortcuts import render

# Create your views here.

def basepage(request):
    return render(request, "base.html")

def homepage(request):
    return render(request, "homepage.html", context={"active":"home"})