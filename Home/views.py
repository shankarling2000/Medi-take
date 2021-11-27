from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")
def test(request):
    return render(request,"test.html")
def contact(request):
    return render(request,"contact.html")
def about(request):
    return render(request,"about.html")