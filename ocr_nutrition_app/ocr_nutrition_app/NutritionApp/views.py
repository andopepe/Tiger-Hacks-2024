from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadImageForm
from django.template import loader
# Create your views here.

from PIL import Image
import io
import base64
from pyzbar.pyzbar import decode

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
        # Check submission type
        submit_type = request.POST.get('submit_type')
        
        if submit_type == 'manual':
            # Handle manual UPC input
            manual_upc = request.POST.get('manual_upc')
            if manual_upc and (len(manual_upc) == 12 or len(manual_upc) == 13):
                return render(request, 'NutritionApp/imageupload.html', {
                    'form': UploadImageForm(),
                    'upc_code': manual_upc
                })
            else:
                return render(request, 'NutritionApp/imageupload.html', {
                    'form': UploadImageForm(),
                    'error': 'Invalid UPC code. Please enter 12 or 13 digits.'
                })
        
        else:
            # Handle image upload
            form = UploadImageForm(request.POST, request.FILES)
            if form.is_valid():
                try:
                    image_file = request.FILES['image']
                    image = Image.open(image_file)
                    
                    # Process the image to detect UPC
                    decoded_objects = decode(image)  # Replace decode with your library function
                    upc_code = None
                    
                    for obj in decoded_objects:
                        # if obj.type == 'UPC_A':  # Uncomment if you want to filter by type
                        upc_code = obj.data.decode('utf-8')
                        break  # Break after finding the first UPC code
                    
                    # Convert image to base64 for display
                    buffered = io.BytesIO()
                    image.save(buffered, format="PNG")
                    img_str = base64.b64encode(buffered.getvalue()).decode()
                    
                    return render(request, 'NutritionApp/imageupload.html', {
                        'form': form,
                        'img_str': img_str,
                        'upc_code': upc_code,
                        'decoded_objects': decoded_objects
                    })
                    
                except Exception as e:
                    print(f"Error processing image: {e}")
                    return render(request, 'NutritionApp/imageupload.html', {
                        'form': form,
                        'error': 'Error processing image'
                    })
            else:
                return render(request, 'NutritionApp/imageupload.html', {
                        'form': form,
                        'error': 'Invalid form submission'
                    })
    
    # GET request - show empty form
    form = UploadImageForm()
    return render(request, 'NutritionApp/imageupload.html', {'form': form})