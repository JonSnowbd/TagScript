from .. import engine
from . import Block
from typing import Optional

class AssignmentBlock(Block):
    def will_accept(self, ctx : engine.Interpreter.Context) -> bool:
        dec = ctx.verb.declaration.lower()
        return any([dec=="=",dec=="assign",dec=="let",dec=="var"])

    def process(self, ctx : engine.Interpreter.Context) -> Optional[str]:
        if ctx.verb.parameter == None:
            return None
        ctx.response.variables[ctx.verb.parameter] = engine.StringAdapter(str(ctx.verb.payload))
        ctx.handled = True
        return ""
