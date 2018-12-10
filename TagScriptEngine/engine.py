class InterpreterContext(object):
    def __init__(self):
        self.verb_tree = []

class Interpreter(object):
    def __init__(self, discord_integration : bool = False):
        self.discord_integration = discord_integration

    async def Start(self) -> InterpreterContext:
        pass