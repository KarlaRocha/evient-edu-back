class UseCase:
    def __init__(self, gateway):
        self.__gateway = gateway

    def execute(self, id, winner):
        return self.__gateway.update_winner(id, winner)
