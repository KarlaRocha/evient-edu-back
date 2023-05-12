class UseCase:
    def __init__(self, gateway):
        self.__gateway = gateway

    def execute(self, args):
        return self.__gateway.get_matches(args)
