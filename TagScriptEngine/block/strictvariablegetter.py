from typing import Optional

from .. import Interpreter, adapter
from ..interface import Block


class StrictVariableGetterBlock(Block):
    def will_accept(self, ctx: Interpreter.Context) -> bool:
        return ctx.verb.declaration in ctx.response.variables

    def process(self, ctx: Interpreter.Context) -> Optional[str]:
        return ctx.response.variables[ctx.verb.declaration].get_value(ctx.verb)
