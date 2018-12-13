from .. import engine
from . import Block
from typing import Optional
import time

class StrfBlock(Block):
    def will_accept(self, ctx : engine.Interpreter.Context) -> bool:
        return ctx.verb.declaration == "strf"

    def process(self, ctx : engine.Interpreter.Context) -> Optional[str]:
        t = time.gmtime()
        if ctx.verb.payload != None:
            result = time.strftime(ctx.verb.payload, t)
            ctx.handled = True
            return result
        else:
            return "`STRF Error, no string supplied.`"
