from django.shortcuts import render
from group14_app.data_api import *
from django.http import HttpResponseRedirect
from .forms import ContactForm


# Create your views here.


def home(request):
    template = "group14_app/homepage.html"

    team_profiles = contacts.get_records()

    group_intros = briefs.get_records()

    return render(request, template, {'team_profiles': team_profiles, 'group_intros': group_intros})


def list(request):

    food_waste_list = items.get_records()

    return render(request, 'group14_app/list.html', {'list': food_waste_list})


def details(request, id):

    # food_waste_list = get_object_or_404(FoodDetail, id=id)
    food_waste_detail = food_details.get_item(id)

    context = {'food_waste_detail': food_waste_detail,
               }
    return render(request, 'group14_app/details.html', context)


def mitigation(request):
    mitigation_strategies = mitigations.get_records()
    return render(request, 'group14_app/mitigation.html', {'mitigation_strategies': mitigation_strategies})


def data_model(request):
    team_profiles = contacts.get_records()
    group_intros = briefs.get_records()
    food_waste_list = items.get_records()
    food_waste_detail = food_details.get_records()
    mitigation_strategies = mitigations.get_records()

    return render(request, 'group14_app/data-model.html', {'group_intros': group_intros, 'team_profiles': team_profiles, 'list': food_waste_list, 'context': food_waste_detail, 'mitigation_strategies': mitigation_strategies})

def contact(request):
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm
        if 'submitted' in request.GET:
            submitted = True    
    form = ContactForm
    return render(request, 'group14_app/contact.html', {'form': form, 'submitted':submitted})