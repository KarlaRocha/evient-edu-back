class UseCase:
    def __init__(self, gateway):
        self._gateway = gateway

    def execute(self, match_id, player_id, cell_id):
        return self._gateway.update_player_move(match_id, player_id, cell_id)