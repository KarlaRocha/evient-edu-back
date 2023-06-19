from match.models import Match
from cell.models import Cell


class Gateway:
    def update_player_move(self, match_id, player_id, cell_id):
        try:
            match = Match.objects.get(pk=match_id)
            cell = Cell.objects.get(pk=cell_id)
            cell.symbol = match.symbol
            cell.save()
            player_turn = self._get_player_turn(player_id, match)
            match.turn = player_turn
            new_symbol = self._get_new_symbol(match)
            match.symbol = new_symbol
            match.save()
            return {"success": True}
        except Exception as ex:
            print(ex)
            return {"success": False}

    # TODO: Move to use case
    def _get_player_turn(self, player_id, match):
        if match.player_1.pk == player_id:
            return match.player_2
        return match.player_1
    
    # TODO: Move to use case
    def _get_new_symbol(self, match):
        if match.symbol == "X":
            return "O"
        return "X"
