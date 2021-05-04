from typing import Optional

from .. import Interpreter, adapter
from ..interface import Block


class LooseVariableGetterBlock(Block):
    def will_accept(self, ctx: Interpreter.Context) -> bool:
        return True

    def process(self, ctx: Interpreter.Context) -> Optional[str]:
        if ctx.verb.declaration in ctx.response.variables:
            return ctx.response.variables[ctx.verb.declaration].get_value(ctx.verb)
        else:
            return None
