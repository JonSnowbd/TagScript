from .. import Interpreter, adapter
from ..interface import Block
from typing import Optional
import random


class RandomBlock(Block):
    def will_accept(self, ctx: Interpreter.Context) -> bool:
        dec = ctx.verb.declaration.lower()
        return any([dec == "random", dec == "#", dec == "rand"])

    def process(self, ctx: Interpreter.Context) -> Optional[str]:
        if ctx.verb.payload is None:
            return None
        spl = []
        if "~" in ctx.verb.payload:
            spl = ctx.verb.payload.split("~")
        else:
            spl = ctx.verb.payload.split(",")
        random.seed(ctx.verb.parameter)

        result = random.choice(spl)
        return result
