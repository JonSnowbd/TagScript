from .. import Interpreter, adapter
from ..interface import Block
from typing import Optional
import random

class RangeBlock(Block):
    def will_accept(self, ctx : Interpreter.Context) -> bool:
        return ctx.verb.declaration == "range"

    def process(self, ctx : Interpreter.Context) -> Optional[str]:
        try:
            spl = ctx.verb.payload.split("-")
            lower = int(spl[0])
            upper = int(spl[1])

            random.seed(ctx.verb.parameter)
            
            value = str(random.randint(lower, upper))
            return value
        except:
            return None
