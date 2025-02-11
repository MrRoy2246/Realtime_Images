from django.urls import re_path
from .consumers import ImageConsumer

websocket_urlpatterns = [
    re_path(r'ws/images/$', ImageConsumer.as_asgi()),  # WebSocket route
]
