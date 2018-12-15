from .. import engine
from . import Block
from typing import Optional
import random

class LooseVariableGetterBlock(Block):
    def will_accept(self, ctx : engine.Interpreter.Context) -> bool:
        return True

    def process(self, ctx : engine.Interpreter.Context) -> Optional[str]:
        if ctx.verb.declaration in ctx.response.variables:
            response = ctx.response.variables[ctx.verb.declaration].get_value(ctx.verb)
            ctx.handled = True
            return response
        else:
            return None

