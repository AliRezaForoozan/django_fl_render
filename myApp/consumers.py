from channels.generic.websocket import AsyncWebsocketConsumer
import json

class TestConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(json.dumps({"message": "connected"}))

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.send(json.dumps({"echo": data}))