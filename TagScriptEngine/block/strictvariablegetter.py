from .. import engine
from . import Block
from typing import Optional
import random

class StrictVariableGetterBlock(Block):
    def will_accept(self, ctx : engine.Interpreter.Context) -> bool:
        return ctx.verb.declaration in ctx.response.variables

    def process(self, ctx : engine.Interpreter.Context) -> Optional[str]:
        ctx.handled = True
        return ctx.response.variables[ctx.verb.declaration].get_value(ctx.verb)
