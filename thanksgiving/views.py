from django.shortcuts import render
from thanksgiving.models import Dish
from django.http import HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 

def home(request):
	if request.method == "POST":
		params = request.POST
		new_dish = Dish(
			category = params["category"], 
			title = params["title"],
			servings = params["servings"],
			prep_time = params["prep_time"],
			source = params["source"])
		new_dish.save()

	all_dishes = Dish.objects.all().order_by('category')
	category_list = Dish.objects.order_by('category').values('category').distinct()

	if len(all_dishes) == 0:
		all_dishes = "0"
		print("No Dishes in database")

	data = {"all_dishes" : all_dishes, "category_list" : category_list}
	
	return render(request, "thanksgiving/home.html", data)

def recipes(request):
	if request.method == "POST":
		params = request.POST
		dish_category = params["dish_category"]
	
	dishes = Dish.objects.filter(category=dish_category)

	data = {"dishes" : dishes, "dish_name" : dish_category}
	print("Len of Dishes: ", len(dishes))

	return render(request, "thanksgiving/recipes.html", data)