import json
import requests
from channels.generic.websocket import AsyncWebsocketConsumer

PEXELS_API_KEY = "9kceFjQ8CRd5CPoYp5b9AnIwElTfdljTILI8zFna0IBxqSXHKif1HwzF"  # Replace with your actual Pexels API Key
PEXELS_URL = "https://api.pexels.com/v1/search?query=nature&per_page=1"

class ImageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send_image()

    async def disconnect(self, close_code):
        pass

    async def send_image(self):
        """Fetch image from Pexels API and send it to the WebSocket client."""
        headers = {"Authorization": PEXELS_API_KEY}
        response = requests.get(PEXELS_URL, headers=headers)

        if response.status_code == 200:
            data = response.json()
            if data["photos"]:
                image_url = data["photos"][0]["src"]["original"]
                await self.send(text_data=json.dumps({"image_url": image_url}))
       
