# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from tablib import Dataset

from .models import ContactInfo
from .forms import ContactInfoForm
from .resources import ContactInfoResource
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required(login_url='/')
def view_home(request):
	contact_info = ContactInfo.objects.filter(created_by=request.user)
	return render(request,'contacts/home.html',{'contact_info':contact_info})

def redirecting(request):
	return redirect('view_home')

@login_required(login_url='/')
def add(request):
	if request.method == "POST":
			form = ContactInfoForm(request.POST)
			if form.is_valid():
				contact = form.save(commit=False)
				contact.created_by = request.user
				contact.save()
				return redirect('view_home')
	else:
		form = ContactInfoForm()
		return render(request, 'contacts/add.html', {'form':form})

@login_required(login_url='/')
def edit(request,pk):
	contact_info = get_object_or_404(ContactInfo,pk=pk)
	if request.method == "POST":
		form = ContactInfoForm(request.POST, instance=contact_info)
		if form.is_valid():
			contact_info=form.save(commit=False)
			contact_info.created_by = request.user
			contact_info.save()
			return redirect('view_home')
	else:
		form = ContactInfoForm(instance=contact_info)
		return render(request,'contacts/add.html',{'form':form})

@login_required(login_url='/')
def displaycontact(request, pk):
	contact_info = get_object_or_404(ContactInfo, pk=pk)
	return render(request, 'contacts/delete.html', {'contact_info':contact_info})

@login_required(login_url='/')
def delete(request,pk):
	contact_info = get_object_or_404(ContactInfo,pk=pk)
	contact_info.delete()
	return redirect('view_home')

def simple_upload(request):
    if request.method == 'POST':
        contact_resource = ContactInfoResource()
        dataset = Dataset()
        new_contacts = request.FILES['myfile']

        imported_data = dataset.load(new_contacts.read())

        person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'contacts/import.html')