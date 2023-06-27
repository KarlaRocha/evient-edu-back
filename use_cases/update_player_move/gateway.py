from datetime import datetime

from match.models import Match
from cell.models import Cell


class Gateway:
    def update_player_move(self, match_id, player_id, cell_id):
        try:
            match = Match.objects.get(pk=match_id)
            cells = self._get_cells(match)
            cell = Cell.objects.get(pk=cell_id)
            cell.symbol = match.symbol
            cell.save()
            player_turn = self._get_player_turn(player_id, match)
            match.turn = player_turn
            new_symbol = self._get_new_symbol(match)
            match.symbol = new_symbol
            match.updated_date = datetime.now()
            match.save()
            cells = self._get_cells(match)
            data = {
                "id": match.id,
                "updated_match": match.updated_date,
                "player_1": {
                    "id": match.player_1.pk,
                    "name": match.player_1.name, 
                    "age": match.player_1.age
                },
                "player_2": {
                    "id": match.player_2.pk,
                    "name": match.player_2.name,
                    "age": match.player_2.age,
                },
                "active": match.active,
                "symbol": match.symbol,
                "winner": self._get_winner(match),
                "turn": self._get_turn(match),
                "is_draw": match.is_draw,
                "cells": cells
            }
            return {"success": True, "errors": None, "data": data}
        except Exception as ex:
            print(ex)
            return {"success": False, "errors": [ex], "data": data}

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
    
    def _get_cells(self, match):
        return [{
            "id": cell.pk,
            "row": cell.row,
            "column": cell.column,
            "symbol": cell.symbol,
        } for cell in match.cell_set.all()]
