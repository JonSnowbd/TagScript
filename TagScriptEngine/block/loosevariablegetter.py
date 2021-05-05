from typing import Optional

from ..interface import Block
from ..interpreter import Context


class LooseVariableGetterBlock(Block):
    def will_accept(self, ctx: Context) -> bool:
        return True

    def process(self, ctx: Context) -> Optional[str]:
        if ctx.verb.declaration in ctx.response.variables:
            return ctx.response.variables[ctx.verb.declaration].get_value(ctx.verb)
        else:
            return None
