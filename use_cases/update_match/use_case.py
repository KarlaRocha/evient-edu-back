class UseCase:
    def __init__(self, gateway):
        self.__gateway = gateway

    def execute(self, id, payload):
        return self.__gateway.update_match(id, payload)
