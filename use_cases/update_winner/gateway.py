from match.models import Match
from player.models import Player


class Gateway:
    def update_winner(self, id, winner):
        try:
            match = Match.objects.get(pk=id)
            winner = Player.objects.get(pk=winner)
            match.winner = winner
            match.active = False
            match.save()
            return {"success": True}
        except Exception as ex:
            print(ex)
            return {"success": False}
    
