from .use_case import UseCase
from .gateway import Gateway


class Controller:
    def create_match(self, payload):
        gateway = Gateway()
        use_case = UseCase(gateway)
        return use_case.execute(payload)