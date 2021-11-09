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

	all_dishes = Dish.objects.all()

	if len(all_dishes) == 0:
		all_dishes = "None"
		print("No Dishes in database")

	data = {"all_dishes" : all_dishes}
	
	return render(request, "thanksgiving/home.html", data)

def recipes(request):
	if request.method == "POST":
		params = request.POST
		input_category = params["category"]
	
	dish = Dish.object.get(category=input_category)

	data = {"Dish" : dish}

	return render(request, "thanksgiving/recipes.html", data)