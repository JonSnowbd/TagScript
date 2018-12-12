from .. import engine
from typing import Optional

class Block(object):
    def __init__(self):
        pass

    def will_accept(self, ctx : engine.Interpreter.Context) -> Optional[bool]:
        return False

    def pre_process(self, ctx : engine.Interpreter.Context):
        return None

    def process(self, ctx : engine.Interpreter.Context) -> Optional[str]:
        return None

    def post_process(self, ctx : engine.Interpreter.Context):
        return None