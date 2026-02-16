from channels.generic.websocket import AsyncWebsocketConsumer
import json

class IoTConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "iot_group"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()
        await self.send(json.dumps({"msg": "connected"}))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)

        # پیام از Flutter: درخواست روشن کردن LED
        if data.get("from") == "flutter" and data.get("action") == "led_on":
            await self.channel_layer.group_send(
                self.group_name,
                {
                    "type": "esp.message",
                    "payload": {"cmd": "led_on"},
                },
            )

            # پیام از Flutter: روشن کردن LED
            if data.get("from") == "flutter" and data.get("action") == "led_on":
                await self.channel_layer.group_send(
                    self.group_name,
                    {
                        "type": "esp.message",
                        "payload": {"cmd": "led_on"},
                    },
                )

            # پیام از Flutter: خاموش کردن LED
            if data.get("from") == "flutter" and data.get("action") == "led_off":
                await self.channel_layer.group_send(
                    self.group_name,
                    {
                        "type": "esp.message",
                        "payload": {"cmd": "led_off"},
                    },
                )
    async def esp_message(self, event):
        await self.send(json.dumps({"to": "esp32", **event["payload"]}))

    async def flutter_message(self, event):
        await self.send(json.dumps({"to": "flutter", **event["payload"]}))