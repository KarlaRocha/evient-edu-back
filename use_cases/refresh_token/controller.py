from .use_case import UseCase
from .gateway import Gateway


class Controller:
    def refresh_token(self, login_data: dict):
        gateway = Gateway()
        use_case = UseCase(gateway)
        return use_case.execute(login_data)