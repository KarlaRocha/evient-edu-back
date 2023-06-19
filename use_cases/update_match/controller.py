from .use_case import UseCase
from .gateway import Gateway


class Controller:
    def update_product(self, id, payload):
        gateway = Gateway()
        use_case = UseCase(gateway)
        return use_case.execute(id, payload)
