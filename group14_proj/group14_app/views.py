from django.shortcuts import render, get_object_or_404
from group14_app.models import FoodDetail
# Create your views here.


def home(request):
    template = "group14_app/homepage.html"
    
    context = {}
    team_profiles = [
        {'name': 'Muhammad Firdaus Roslan',
            'id': 'S328473', 'attendance': 'External'},
        {'name': 'Emily Wai Sum Tsang',
            'id': 'S344909', 'attendance': 'External'},
        {'name': 'Amila Kolamba Arachchige',
            'id': 'S356967', 'attendance': 'External'},
        {'name': 'I Putu Mahesa Gangga Wisuda',
            'id': 'S355549', 'attendance': 'External'},
    ]
    
    info = {}
    group_intros = [
        {'brief' : 'Welcome to our website which is focused on food waste and mitigation! We are dedicated to addressing one of the pressing global issues of our time: food waste. Every year, billions of tons of food are wasted worldwide, contributing to environmental, social, and economic challenges, especially in Australia. Our website serves as a comprehensive resource for individuals, businesses, and communities seeking information and solutions to reduce food waste and its impacts. From practical tips on reducing food waste at home, to innovative strategies for businesses and policymakers, our website offers a wealth of knowledge, tools, and resources to promote sustainable practices and mitigate the adverse effects of food waste. Join us in the fight against food waste, and together, we can make a positive impact on our planet and society. Explore our website and discover how you can contribute to the global effort to reduce food waste and create a more sustainable future for all.'},
    ]

    context['team_profiles'] = team_profiles
    info['group_intros'] = group_intros
    return render (request, template, {'team_profiles': team_profiles, 'group_intros': group_intros})


def list(request):
    food_waste_list = [
        {
            'type': 'Household waste',
            'description': 'This is the food waste that occurs in our homes, including food that is left uneaten on plates, expired or spoiled food, and food that is thrown away because it is no longer wanted.',
            'id': '1'
        },
        {
            'type': 'Retail waste',
            'description': 'This includes food that is thrown away by supermarkets, grocery stores, and other food retailers due to overstocking, expiration, or damage.',
            'id': '2'
        },
        {
            'type': 'Restaurant waste',
            'description': 'This is the food waste that occurs in restaurants, cafes, and other food service establishments, including food that is left uneaten by customers, overproduction, and spoilage.',
            'id': '3'
        },
        {
            'type': 'Agricultural waste',
            'description': 'This includes food that is lost during the production and harvesting of crops, such as fruits and vegetables that are left in the field due to overproduction or damage.',
            'id': '4'
        },
        {
            'type': 'Processing waste',
            'description': 'This is the food waste that occurs during the processing and manufacturing of food products, including scraps, trimmings, and packaging waste.',
            'id': '5'
        },
        {
            'type': 'Transportation and distribution waste',
            'description': 'This includes food that is lost during transportation and distribution, such as spoilage and damage during transit.',
            'id': '6'
        },
    ]

    return render(request, 'group14_app/list.html', {'list': food_waste_list})


def details(request, id):
    food_waste_list = get_object_or_404(FoodDetail, id=id)

    context = {'food_waste_list': food_waste_list,
               }
    return render(request, 'group14_app/details.html', context)


def data_model(request):
    return render(request, 'group14_app/data-model.html')
