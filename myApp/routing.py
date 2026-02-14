from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/myApp/', consumers.TestConsumer.as_asgi()),
]