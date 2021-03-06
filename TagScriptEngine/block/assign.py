from .. import Interpreter, adapter
from ..interface import Block
from typing import Optional


class AssignmentBlock(Block):
    def will_accept(self, ctx: Interpreter.Context) -> bool:
        dec = ctx.verb.declaration.lower()
        return any([dec == "=", dec == "assign", dec == "let", dec == "var"])

    def process(self, ctx: Interpreter.Context) -> Optional[str]:
        if ctx.verb.parameter == None:
            return None
        ctx.response.variables[ctx.verb.parameter] = adapter.StringAdapter(str(ctx.verb.payload))
        return ""
