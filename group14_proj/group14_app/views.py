from django.shortcuts import render, get_object_or_404
from group14_app.models import FoodDetail
from group14_app.table import *

# Create your views here.


def home(request):
    template = "group14_app/homepage.html"

    team_profiles = contacts.records
    
    group_intros = briefs.records

    return render (request, template, {'team_profiles': team_profiles, 'group_intros': group_intros})


def list(request):
    # food_waste_list = [
    #     {
    #         'type': 'Household waste',
    #         'description': 'This is the food waste that occurs in our homes, including food that is left uneaten on plates, expired or spoiled food, and food that is thrown away because it is no longer wanted.',
    #         'id': '1'
    #     },
    #     {
    #         'type': 'Retail waste',
    #         'description': 'This includes food that is thrown away by supermarkets, grocery stores, and other food retailers due to overstocking, expiration, or damage.',
    #         'id': '2'
    #     },
    #     {
    #         'type': 'Restaurant waste',
    #         'description': 'This is the food waste that occurs in restaurants, cafes, and other food service establishments, including food that is left uneaten by customers, overproduction, and spoilage.',
    #         'id': '3'
    #     },
    #     {
    #         'type': 'Agricultural waste',
    #         'description': 'This includes food that is lost during the production and harvesting of crops, such as fruits and vegetables that are left in the field due to overproduction or damage.',
    #         'id': '4'
    #     },
    #     {
    #         'type': 'Processing waste',
    #         'description': 'This is the food waste that occurs during the processing and manufacturing of food products, including scraps, trimmings, and packaging waste.',
    #         'id': '5'
    #     },
    #     {
    #         'type': 'Transportation and distribution waste',
    #         'description': 'This includes food that is lost during transportation and distribution, such as spoilage and damage during transit.',
    #         'id': '6'
    #     },
    # ]
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
