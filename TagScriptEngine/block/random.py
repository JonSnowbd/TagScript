from .. import engine
from . import Block
from typing import Optional
import random

class RandomBlock(Block):
    def will_accept(self, ctx : engine.Interpreter.Context) -> bool:
        dec = ctx.verb.declaration.lower()
        return any([dec == "random", dec == "#", dec =="rand"])

    def process(self, ctx : engine.Interpreter.Context) -> Optional[str]:
        spl = []
        if "~" in ctx.verb.payload:
            spl = ctx.verb.payload.split("~")
        else:
            spl = ctx.verb.payload.split(",")
        if ctx.verb.parameter is not None:
            random.seed(ctx.verb.parameter)

        result = random.choice(spl)
        ctx.handled = True
        return result
