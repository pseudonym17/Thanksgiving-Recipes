from django.contrib import admin
from thanksgiving.models import Dish
from thanksgiving.models import Ingredient

# Register your models here.
admin.site.register(Dish)
admin.site.register(Ingredient)