from .use_case import UseCase
from .gateway import Gateway


class Controller:
    def update_winner(self, id, winner):
        gateway = Gateway()
        use_case = UseCase(gateway)
        return use_case.execute(id, winner)
