from django.shortcuts import render
from django.apps import apps
from .models import *
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.db import models
from django.urls import reverse



#dictionry to map model classes to their corresponding Forms 
MODELE_FORMS = {Organization:FormOrganization, User:FormUser, Location:FormLocation, WasteCat:FormWasteCat, WasteItem:FormWasteItem, WasteLog:FormWasteLog}

def get_model_record_to_form(request,model='',pk=''):
    model_class = apps.get_model('admin_g14',model)
    a = model_class.objects.get(pk=pk)
    form = MODELE_FORMS[model_class](request.POST,instance=a)
    return form

def model_list(request):
    APP_LABEL = 'admin_g14'
    app_models = apps.all_models[APP_LABEL]
    APP_MODELS = [
    model.__name__ for model in app_models.values()
    if not model._meta.auto_created 
    ]
    return render(request, 'admin_g14/admin.html',{'app_models':APP_MODELS})

def create(request,model=''):
    model_class = apps.get_model('admin_g14',model)
    submitted = False
    if request.method =='POST':
        form = MODELE_FORMS[model_class](request.POST)
        if form.is_valid():
            instance= form.save()
            return render(request,'admin_g14/cred.html', {'f':form,'submitted':True,'create':True,'pk':instance.pk,'model':model,'name':instance.name})
            # return HttpResponseRedirect('?submitted=True')
    else:
        form = MODELE_FORMS[model_class]()
        if 'submitted' in request.GET:
            submitted = True 
    return render(request,'admin_g14/cred.html', {'f':form,'submitted':submitted,'create':True})

def view(request,model=''):
    model_class = apps.get_model('admin_g14',model)
    rows = model_class.objects.filter()
    if not rows.exists():
        return HttpResponse("no records found.<br><a href ='/admin-home'>Go to Admin home Page<br>")
    else:
        return render(request,'admin_g14/cred.html',{'rows':rows,'model':model,'view':True,'delete':False})
    
def edit(request,model='',pk=''):
    model_class = apps.get_model('admin_g14',model)
    a = model_class.objects.get(pk=pk)
    form = MODELE_FORMS[model_class](instance=a)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    return render(request,'admin_g14/edit.html',{'editform':form,'model':model, 'edit':True,'pk':pk})

def save(request, model='',pk=''):
    if request.method == 'POST':
        model_class = apps.get_model('admin_g14',model)
        a = model_class.objects.get(pk=pk)
        form=MODELE_FORMS[model_class](request.POST,instance=a)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/admin-home')
 
def delete(request,model=''):
    error=''
    model_class = apps.get_model('admin_g14',model)
    rows = model_class.objects.filter()
    if request.method == 'POST':
        list_of_deleted_row_pk=request.POST.getlist('inputs')
        if len(list_of_deleted_row_pk)==0:
            error = 'Items must be selected in order to perform actions on them. No items have been changed.'
            return render(request,'admin_g14/cred.html',{'rows':rows,'model':model,'view':False,'delete':True,'error':error})
        else:
            for i in list_of_deleted_row_pk:
                model_class.objects.get(id=i).delete()
            return render(request,'admin_g14/cred.html',{'rows':rows,'model':model,'view':False,'delete':True,'error':error})
    else:
        if not rows.exists():
            return HttpResponse("no records found.<br><a href ='/admin-home'>Go to Admin home Page<br>")
        else:
            return render(request,'admin_g14/cred.html',{'rows':rows,'model':model,'view':False,'delete':True,'error':error})
