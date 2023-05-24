from match.models import Match


class Gateway:
    def get_match(self, id):
        try:
            match = Match.objects.get(pk=id)
            cells = self._get_cells(match)
            return {
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
        except Exception as ex:
            print(ex)
            return None
        
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
