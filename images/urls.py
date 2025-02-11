from django.urls import path
from .views import get_new_image,image_view

urlpatterns = [
    path("test/", image_view, name="test"),
    path("get-new-image/", get_new_image, name="get_new_image"),
]
