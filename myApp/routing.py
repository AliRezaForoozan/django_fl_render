from django.urls import path
from myApp.consumers import StatusConsumer

websocket_urlpatterns = [
    path("ws/status/", StatusConsumer.as_asgi()),
]
