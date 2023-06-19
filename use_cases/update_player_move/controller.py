from .use_case import UseCase
from .gateway import Gateway


class Controller:
    def update_player_move(self, match_id, player_id, cell_id):
        gateway = Gateway()
        use_case = UseCase(gateway)
        return use_case.execute(match_id, player_id, cell_id)