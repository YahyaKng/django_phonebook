from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import PhonebookForm
from .models import Phonebook

def index(request):  
    records = Phonebook.objects.all()  
    return render(request,"core/index.html",{'records':records})  

def new(request):  
    if request.method == "POST":  
        form = PhonebookForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                raise ValueError('Error while saving phonebook record')
        else:
            messages.error(request, 'Invalid')
    else:  
        form = PhonebookForm()  
    return render(request,'core/new.html',{'form':form}) 

def edit(request, id):  
    record = Phonebook.objects.get(id=id)  
    return render(request,'core/edit.html', {'record':record})  

def update(request, id):  
    record = Phonebook.objects.get(id=id)  
    form = PhonebookForm(request.POST, instance = record)  
    if form.is_valid():  
        form.save()  
        return redirect("/")
    else:
        messages.error(request, 'Invalid')
    return render(request, 'core/edit.html', {'record': record})  

def destroy(request, id):  
    records = Phonebook.objects.get(id=id)  
    records.delete()  
    return redirect("/")  
