from channels.generic.websocket import AsyncWebsocketConsumer

class PlayerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Connect to the WebSocket
        await self.accept()

    async def disconnect(self, close_code):
        # Disconnect from the WebSocket
        pass

    async def notify_new_player(self, event):
        # Send new player notification to WebSocket client
        await self.send(text_data=event['message'])
