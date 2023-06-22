import json
import pandas as pd
from django.shortcuts import render, HttpResponse
from . models import * 
from django.db.models import Q

# Create your views here.

def index(request):
    items = ''  # Default value for 'items'
    search_item = None  # Default value for 'search_item'

    if request.method == 'POST':
        items = request.POST.get('search', '')
        searched = Q(Q(name__icontains=items) | Q(Q(price__icontains=items)))
        search_item = FoodItem.objects.filter(searched)

    context = {
        'items': items,
        'search_item':search_item,

    }
    return render(request, 'index.html', context)


# Views to extract data from csv file into database
# def extract(file_path):
#     df = pd.read_csv(file_path)  # Read the CSV file into a DataFrame
#     for _, row in df.iterrows():  # Iterate over each row in the DataFrame
#         items_dict = json.loads(row['items'])  # Convert the string dictionary to a Python dictionary

#         my_model = Food.objects.create(
#             name=row['name'], 
#             location=row['location'], 
#             lat_long=row['lat_long'], 
#             full_details=row['full_details']
#         )

#         for item_name, item_price in items_dict.items():
#             food_item, _ = FoodItem.objects.get_or_create(
#                 name=item_name.strip(), 
#                 price=item_price.strip()
#             )
#             my_model.items.add(food_item)
# csv_file_path = 'home/data/restaurants_small.csv'  # Replace with the actual path to your CSV file
# extract(csv_file_path)
