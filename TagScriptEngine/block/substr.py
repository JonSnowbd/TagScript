from .. import Interpreter, adapter
from ..interface import Block
from typing import Optional


class SubstringBlock(Block):
    def will_accept(self, ctx: Interpreter.Context) -> bool:
        dec = ctx.verb.declaration.lower()
        return any([dec == "substr", dec == "substring"])

    def process(self, ctx: Interpreter.Context) -> Optional[str]:
        try:

            if "-" in ctx.verb.parameter:
                spl = ctx.verb.parameter.split("-")
                start = int(float(spl[0]))
                end = int(float(spl[1]))

                return ctx.verb.payload[start:end]
            else:
                start = int(float(ctx.verb.parameter))

                return ctx.verb.payload[start:]
        except:
            return None
