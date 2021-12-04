from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import ContactForms
from mainclass import ptsd,adder,sleepness,adhd,stress,depression
import time

# Create your views here.
def test(request):
    if request.method =='POST':
        form=ContactForms(request.POST)
    context ={}
    context['form']= ContactForms()
    psyc_test_res= request.POST.getlist('display_type[]')
    print("psyc test res")
    print(psyc_test_res)
    with open("myfile.txt", "a") as file1:
        # Writing data to a file
        t=time.strftime('%a %H:%M:%S')
        file1.write(f"{psyc_test_res},{t}")
    
    adder(psyc_test_res)
    print(sleepness.clicks)
    print(adhd.clicks)
    print(stress.clicks)
    print(ptsd.clicks)
    print(depression.clicks)

    return render(request, "index.html", context)

def index(request):
    return render(request,"test.html")
def contact(request):
    return render(request,"contact.html")
def about(request):
    return render(request,"about.html")

