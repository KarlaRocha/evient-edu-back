class UseCase:
    def __init__(self, gateway):
        self._gateway = gateway

    def execute(self, login_data: dict):
        return self._gateway.refresh_token(login_data)
