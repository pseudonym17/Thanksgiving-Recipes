from django.db import models

# Create your models here.

class Ingredient(models.Model):
	ingredient = models.CharField(max_length=100)
	amount = models.CharField(max_length=10)

class Dish(models.Model):
	title = models.CharField(max_length=100)
	prep_time = models.CharField(max_length=10)
	servings = models.IntegerField()
	source = models.CharField(max_length=265)
	#directions = models.CharField(max_length=2048)
	category = models.CharField(max_length=100)
	#ingredient = models.ManyToManyField(Ingredient)
