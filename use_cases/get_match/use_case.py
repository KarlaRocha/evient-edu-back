class UseCase:
    def __init__(self, gateway) -> None:
        self._gateway = gateway

    def execute(self, id):
        return self._gateway.get_match(id)
