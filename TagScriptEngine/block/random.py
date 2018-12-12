from .. import engine
from . import Block
from typing import Optional
import random

class RandomBlock(Block):
    def will_accept(self, ctx : engine.Interpreter.Context) -> bool:
        return ctx.verb.declaration == "random"

    def process(self, ctx : engine.Interpreter.Context) -> Optional[str]:
        ctx.handled = True
        spl = ctx.verb.payload.split("~")
        if ctx.verb.parameter is not None:
            random.seed(ctx.verb.parameter)
        return random.choice(spl)
