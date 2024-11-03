import requests

API_KEY = open("ocr_nutrition_app/NutritionApp/api/api_key.txt").read()

def get_all_data(barcode):
    # Returns 
    if type(barcode) != str:
        barcode = str(barcode)
    
    url = F"https://api.barcodelookup.com/v3/products?barcode={barcode}&formatted=y&key={API_KEY}"
    response = requests.get(url)
    
    # Barcode not found
    if response.status_code == 404:
        return None
    
    return response.json()
