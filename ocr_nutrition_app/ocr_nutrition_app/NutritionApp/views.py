from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadImageForm
from django.template import loader


from PIL import Image
import io
import base64
from pyzbar.pyzbar import decode
from .api.api import get_all_data
# Create your views here.


def index(request):
    return render(request, "NutritionApp/index.html")

def handle_manual_upc(request):
    """Handles manual UPC input."""
    manual_upc = request.POST.get('manual_upc')
    if manual_upc and len(manual_upc) in (12, 13):
        return {
            'form': UploadImageForm(),
            'upc_code': manual_upc
        }
    return {
        'form': UploadImageForm(),
        'error': 'Invalid UPC code. Please enter 12 or 13 digits.'
    }
    
def handle_image_upload(request):
    """Handles image upload for UPC code detection."""
    form = UploadImageForm(request.POST, request.FILES)
    if not form.is_valid():
        return {
            'form': form,
            'error': 'Invalid form submission'
        }

    try:
        image_file = request.FILES['image']
        image = Image.open(image_file)
        
        # Decode UPC from image
        decoded_objects = decode(image)
        upc_code = next((obj.data.decode('utf-8') for obj in decoded_objects), None)
        
        # Convert image to base64 for display
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        # Check if UPC code was detected
        if not upc_code:
            return {
                'form': form,
                'img_str': img_str,
                'error': 'No UPC code detected in the uploaded image.'
            }
        
        return {
            'form': form,
            'img_str': img_str,
            'upc_code': upc_code,
            'decoded_objects': decoded_objects
        }
    except Exception as e:
        print(f"Error processing image: {e}")
        return {
            'form': form,
            'error': 'Error processing image'
        }


def Upload(request):
    if request.method == 'POST':
        submit_type = request.POST.get('submit_type')
        
        if submit_type == 'manual':
            context = handle_manual_upc(request)
        else:
            context = handle_image_upload(request)
        
        return render(request, 'NutritionApp/imageupload.html', context)
    
    # GET request - show empty form
    return render(request, 'NutritionApp/imageupload.html', {'form': UploadImageForm()})

def statistics_view(request, upc):
    data = get_all_data(upc)
    
    if data is None:
        return render(request, 'NutritionApp/not_found.html', {'upc': upc})  # Handle UPC not found
    
    product_info = data.get('products', [{}])[0]
    product_name = product_info.get('product_name', 'Unknown Product')
    nutrition = product_info.get('nutritional_info', {})
    
    context = {
        'upc': upc,
        'product_name': product_name,
        'nutrition': nutrition,
    }
    
    return render(request, 'NutritionApp/statistics.html', context)