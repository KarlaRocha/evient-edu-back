from .use_case import UseCase
from .gateway import Gateway


class Controller:
    def get_match(self, id):
        gateway = Gateway()
        use_case = UseCase(gateway)
        return use_case.execute(id)