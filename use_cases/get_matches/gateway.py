from django.db.models import Q

from match.models import Match


class Gateway:
    def get_matches(self, args):
        try:
            matches = Match.objects.all()
            matches = self._apply_filters(args, matches)
            matches = [{
                "id": data.id,
                "updated_data": data.updated_date,
                "player_1": {
                    "id": data.player_1.pk,
                    "name": data.player_1.name, 
                    "age": data.player_1.age
                },
                "player_2": {
                    "id": data.player_2.pk,
                    "name": data.player_2.name,
                    "age": data.player_2.age,
                },
                "active": data.active,
                "symbol": data.symbol,
                "winner": self._get_winner(data),
                "turn": self._get_turn(data),
                "is_draw": data.is_draw
            } 
            for data in matches]
            return matches
        except Exception as ex:
            print(ex)
            return None
        
    def _apply_filters(self, args, matches):
        if args["active"] is not None:
            matches = matches.filter(active=args["active"])
        if args["player"] is not None:
            matches = matches.filter(Q(player_1=args["player"]) | Q(player_2=args["player"]))
        return matches
    
    def _get_winner(self, data):
        winner = data.winner
        if winner is not None:
            winner = winner.pk
        return winner
    
    def _get_turn(self, data):
        turn = data.turn
        if turn is not None:
            turn = turn.pk
        return turn
    
    def _get_cells(self, data):
        cells = data.cell_set.all()
        return [{
            "id": cell.pk,
            "row": cell.row,
            "column": cell.column,
            "symbol": cell.symbol,
        } for cell in cells]