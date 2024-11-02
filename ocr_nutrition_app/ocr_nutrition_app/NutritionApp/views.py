from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    f = open("ocr_nutrition_app/NutritionApp/frontend/index.html")
    return HttpResponse(f.read())
