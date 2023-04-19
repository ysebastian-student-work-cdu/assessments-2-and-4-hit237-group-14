from django.shortcuts import render, get_object_or_404
from group14_app.models import FoodDetail
from group14_app.data_api import *
# from group14_app.schema import *

# Create your views here.


def home(request):
    template = "group14_app/homepage.html"

    team_profiles = contacts.records
    
    group_intros = briefs.records

    return render (request, template, {'team_profiles': team_profiles, 'group_intros': group_intros})


def list(request):

    food_waste_list = items.records

    return render(request, 'group14_app/list.html', {'list': food_waste_list})


def details(request, id):
    food_waste_list = get_object_or_404(FoodDetail, id=id)

    context={'food_waste_list':food_waste_list,
             }
    return render(request, 'group14_app/details.html', context)


def mitigation(request):
    mitigation_strategies = mitigations.records

    return render(request,'group14_app/mitigation.html', {'mitigation_strategies':mitigation_strategies})

def data_model(request):
    food_waste_list = items.records 
    team_profiles = contacts.records
    group_intros = briefs.records
    mitigation_strategies = mitigations.records

    return render(request, 'group14_app/data-model.html', {'list': food_waste_list, 'group_intros': group_intros, 'team_profiles': team_profiles, 'mitigation_strategies': mitigation_strategies})
