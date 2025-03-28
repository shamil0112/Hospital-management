from django.shortcuts import render
from .models import Departments, Doctors
from .form import BookingForm
# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'conformation.html')
    form = BookingForm()
    dict_form = {
        'form' : form
    }
    return render(request,'booking.html', dict_form)

def doctors(request):
    
    dect_docs = {
        'doctors' : Doctors.objects.all()
    }
    return render(request,'doctors.html',dect_docs)

def contact(request):
    return render(request,'contact.html')

def department(request):
    dict_dept = {
        'dept':Departments.objects.all()
    }
    return render(request,'deparment.html',dict_dept)