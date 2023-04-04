from django.shortcuts import render

# Create your views here.

def home (request):
    return render (request, 'group14_app/homepage.html') 

def list (request):
    return render (request, 'group14_app/list.html') 

def details (request):
    return render (request, 'group14_app/details.html') 

def data_model (request):
    return render (request, 'group14_app/data-model.html') 
