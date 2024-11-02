from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.cache import cache_page
# Create your views here.

def index(request):
    return render(request, "NutritionApp/index.html")
@cache_page(30)
def cached(request):
    user_model = get_user_model()
    all_users = user_model.objects.all()
    return HttpResponse('<html><body><h1>{0} users .. cached</h1></body></html>'.format(len(all_users)))

def cacheless(request):
    user_model = get_user_model()
    all_users = user_model.objects.all()
    return HttpResponse('<html><body><h1>{0} users .. cacheless</h1></body></html>'.format(len(all_users)))
