from typing import Optional

from ..interface import Block
from ..interpreter import Context


class StrictVariableGetterBlock(Block):
    def will_accept(self, ctx: Context) -> bool:
        return ctx.verb.declaration in ctx.response.variables

    def process(self, ctx: Context) -> Optional[str]:
        return ctx.response.variables[ctx.verb.declaration].get_value(ctx.verb)
