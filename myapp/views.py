from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from .models import Hospital

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def learn(request):
    return render(request, 'learn.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def hospital_list(request):
    hospitals = Hospital.objects.all()
    return render(request, 'hospitals.html', {'hospitals': hospitals})

def hospital_create(request):
    if request.method == 'POST':
        hospital = Hospital(
            name=request.POST['name'],
            address=request.POST['address'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            city=request.POST['city'],
            services=request.POST['services'],
            website=request.POST.get('website', '')
        )
        hospital.save()
        return redirect('hospital_list')
    return render(request, 'hospital_form.html')

def hospital_edit(request, pk):
    hospital = get_object_or_404(Hospital, pk=pk)
    if request.method == 'POST':
        hospital.name = request.POST['name']
        hospital.address = request.POST['address']
        hospital.phone = request.POST['phone']
        hospital.email = request.POST['email']
        hospital.city = request.POST['city']
        hospital.services = request.POST['services']
        hospital.website = request.POST.get('website', '')
        hospital.save()
        return redirect('hospital_list')
    return render(request, 'hospital_form.html', {'hospital': hospital})

def hospital_delete(request, pk):
    hospital = get_object_or_404(Hospital, pk=pk)
    if request.method == 'POST':
        hospital.delete()
        return redirect('hospital_list')
    return render(request, 'hospital_confirm_delete.html', {'hospital': hospital})
