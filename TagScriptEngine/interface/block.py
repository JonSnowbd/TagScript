from typing import Optional


class Block(object):
    def __init__(self):
        pass

    def will_accept(self, ctx: "Interpreter.Context") -> Optional[bool]:
        return False

    def pre_process(self, ctx: "Interpreter.Context"):
        return None

    def process(self, ctx: "Interpreter.Context") -> Optional[str]:
        return None

    def post_process(self, ctx: "Interpreter.Context"):
        return None
