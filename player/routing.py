from django.urls import re_path
from .consumers import PlayerConsumer

websocket_urlpatterns = [
    re_path(r'ws/players/$', PlayerConsumer.as_asgi()),
]
