from .. import engine
from . import Block
from typing import Optional
import random

class FiftyFiftyBlock(Block):
    def will_accept(self, ctx : engine.Interpreter.Context) -> bool:
        return ctx.verb.declaration == "5050" or ctx.verb.declaration == "50"

    def process(self, ctx : engine.Interpreter.Context) -> Optional[str]:
        return random.choice(["", ctx.verb.payload])
