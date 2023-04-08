from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'group14_app/homepage.html')


def list(request):
    food_waste_list = [
        {
            'type': 'Household waste',
            'description': 'This is the food waste that occurs in our homes, including food that is left uneaten on plates, expired or spoiled food, and food that is thrown away because it is no longer wanted.',
        },
        {
            'type': 'Retail waste',
            'description': 'This includes food that is thrown away by supermarkets, grocery stores, and other food retailers due to overstocking, expiration, or damage.',
        },
        {
            'type': 'Restaurant waste',
            'description': 'This is the food waste that occurs in restaurants, cafes, and other food service establishments, including food that is left uneaten by customers, overproduction, and spoilage.',
        },
        {
            'type': 'Agricultural waste',
            'description': 'This includes food that is lost during the production and harvesting of crops, such as fruits and vegetables that are left in the field due to overproduction or damage.',
        },
        {
            'type': 'Processing waste',
            'description': 'This is the food waste that occurs during the processing and manufacturing of food products, including scraps, trimmings, and packaging waste.',
        },
        {
            'type': 'Transportation and distribution waste',
            'description': 'This includes food that is lost during transportation and distribution, such as spoilage and damage during transit.',
        },
    ]
    return render(request, 'group14_app/list.html', {'list': food_waste_list} )


def details(request):
    return render(request, 'group14_app/details.html')


def data_model(request):
    return render(request, 'group14_app/data-model.html')
