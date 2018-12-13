from .. import engine, verb
from . import Block
from typing import Optional

class ShortCutRedirectBlock(Block):
    def __init__(self, var_name):
        self.redirect_name = var_name

    def will_accept(self, ctx : engine.Interpreter.Context) -> bool:
        return ctx.verb.declaration.isdigit()

    def process(self, ctx : engine.Interpreter.Context) -> Optional[str]:
        if ctx.handled == True:
            return None

        ctx.verb = verb.VerbContext(self.redirect_name, None, ctx.verb.declaration)

        return None

