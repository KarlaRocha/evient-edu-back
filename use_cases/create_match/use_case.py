class UseCase:
    def __init__(self, gateway):
        self._gateway = gateway

    def execute(self, payload):
        return self._gateway.create_match(payload)