from django.urls import path
from myApp.consumers import IoTConsumer

websocket_urlpatterns = [
    path("ws/iot/", IoTConsumer.as_asgi()),
]