async def receive(self, text_data):
    data = json.loads(text_data)

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

    # پیام از ESP32
    if data.get("from") == "esp32":
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "flutter.message",
                "payload": data,
            },
        )