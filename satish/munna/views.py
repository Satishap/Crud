from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *

def index(request):
    obj = tudent.objects.all()
    return render(request, 'index.html',{'obj':obj})

def detail(request):
    obj1 = get_object_or_404(tudent)
    return render(request, 'detail.html', {'obj':obj1})


def customer(request):
    obj = Customer.objects.all()
    return render(request,"customer.html",{'obj':obj})    

def image(request):
    obj = Satish.objects.all()
    return render(request,"image.html",{'obj':obj})  
def reg(request):
    return render(request,"reg.html")  

def hello(request):
	return render(request,'hello.html')



def Hyy(request):
	if request.method == 'POST':
		form=Hello_form(request.POST or None)
		if form.is_valid():
			form.save()
			return redirect(hello)
	else:
		form= Hello_form()
	return render(request,"Hyy.html",{'form':form})			



def service(request):
	if request.method == 'POST':
		form = Customer_form(request.POST or None)
		if form.is_valid():
			form.save()
			return redirect(hello)
	else:
		form = Customer_form()
	return render(request,"service.html",{'form':form})						

def website(request):
	obj=Customer.objects.all()
	return render(request, "Website.html",{'obj':obj})

def Navbar(request):
	if request.method =='POST':
		form = Navbar_form(request.POST or None)
		if form.is_valid():
			form.save()
			return redirect(hello)
	else:
		form=Navbar_form()	
	return render(request,"Navbar.html",{'form':form})		


