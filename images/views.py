import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.cache import never_cache
PEXELS_API_KEY = "9kceFjQ8CRd5CPoYp5b9AnIwElTfdljTILI8zFna0IBxqSXHKif1HwzF"
# ✅ View to render the HTML template
def image_view(request):
    return render(request, "images/test.html")  # Renders test.html from templates/images folder

# ✅ API View to fetch a new image from Pexels
@never_cache  # This decorator ensures the response is not cached
def get_new_image(request):
    PEXELS_API_KEY = '9kceFjQ8CRd5CPoYp5b9AnIwElTfdljTILI8zFna0IBxqSXHKif1HwzF'  # Make sure to replace this with your actual API key
    if not PEXELS_API_KEY:
        return JsonResponse({"error": "API Key is missing"}, status=400)

    url = "https://api.pexels.com/v1/search?query=nature&per_page=1"
    headers = {"Authorization": PEXELS_API_KEY}
    response = requests.get(url, headers=headers)

    # Check if the response status is OK (200)
    if response.status_code == 200:
        data = response.json()
        # Ensure we have data in the "photos" field
        if data.get("photos"):
            # Fetch the image URL
            image_url = data["photos"][0]["src"]["medium"]
            return JsonResponse({"image_url": image_url})

    # In case of failure, return a 500 error with the appropriate message
    return JsonResponse({"error": "Failed to fetch image"}, status=500)






