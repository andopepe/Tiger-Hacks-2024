from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadImageForm
from django.template import loader
from django.views.decorators.cache import cache_page
# Create your views here.

from PIL import Image
import io
import base64
# from pyzbar.pyzbar import decode

def index(request):
    return render(request, "NutritionApp/index.html")

# @cache_page(30)
# def cached(request):
#     user_model = get_user_model()
#     all_users = user_model.objects.all()
#     return HttpResponse('<html><body><h1>{0} users .. cached</h1></body></html>'.format(len(all_users)))

# def cacheless(request):
#     user_model = get_user_model()
#     all_users = user_model.objects.all()
#     return HttpResponse('<html><body><h1>{0} users .. cacheless</h1></body></html>'.format(len(all_users)))

def Upload(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = request.FILES['image']
            image = Image.open(image_file)
            # Perform any image processing with Pillow here if needed

            # Convert the image to base64 for rendering in HTML
            buffered = io.BytesIO()
            image.save(buffered, format="PNG")

            # pyzbar

            img_str = base64.b64encode(buffered.getvalue()).decode()

            return render(request, 'NutritionApp/imageupload.html', {'form': form, 'img_str': img_str})
    else:
        form = UploadImageForm()
    return render(request, 'NutritionApp/imageupload.html', {'form': form})