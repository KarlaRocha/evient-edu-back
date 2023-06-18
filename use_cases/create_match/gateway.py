import datetime

from match.models import Match
from player.models import Player
from cell.models import Cell


class Gateway:
    def create_match(self, payload):
        try:
            now = datetime.datetime.now()
            player_1 = Player.objects.get(pk=payload['player_1_id'])
            player_2 = Player.objects.get(pk=payload['player_2_id'])
            match = Match.objects.create(
                player_1=player_1,
                player_2=player_2,
                active=True,
                symbol="X",
                turn=player_1,
                created_date=now,
                updated_date=now
            )
            self._add_cells(match)
            match.save()
            return match.pk
        except Exception as ex:
            print(ex)
            return ex
        
    def _add_cells(self, match):
        if match is None: pass
        new_cells = []
        for row in range(0, 3):
            for column in range(0, 3):
                cell = Cell(
                    row=row,
                    column=column,
                    symbol="",
                    match=match,
                )
                new_cells.append(cell)
        Cell.objects.bulk_create(new_cells)