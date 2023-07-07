from channels.generic.websocket import AsyncWebsocketConsumer

class MatchConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("Match websocket connected. match_group")
        match_group = "match_group"
        self.match_group = match_group
        await self.channel_layer.group_add(
            match_group, self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        print("Match websocket disconnected match_group")
        print(self)
        print(close_code)

    async def receive(self, text_data):
        print("Receiving message from match websocket match_group")
        print(self)
        print('text_data',text_data)
        await self.channel_layer.group_send(
            self.match_group, {
                "type": "notify_player_move",
                "text": text_data
            }
        )

    async def notify_player_move(self, event):
        # Send new player notification to WebSocket client
        print("notify_player_move A")
        print(event)
        await self.send(text_data=event['message'])


class MatchListConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("Match websocket connected.")
        matches_group = "matches_group"
        self.matches_group = matches_group
        await self.channel_layer.group_add(
            matches_group, self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        print("Match websocket disconnected")
        print(self)
        print(close_code)

    async def receive(self, text_data):
        print("Receiving message from match websocket")
        print(self)
        print(text_data)
        await self.channel_layer.group_send(
            self.matches_group, {
                "type": "marches_message",
                "text": text_data
            }
        )

    async def notify_new_march(self, event):
        # Send new player notification to WebSocket client
        print("notify_new_march")
        print(event)
        await self.send(text_data=event['message'])