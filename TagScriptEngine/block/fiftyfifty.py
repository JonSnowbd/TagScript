from .. import Interpreter, adapter
from ..interface import Block
from typing import Optional
import random

class FiftyFiftyBlock(Block):
    def will_accept(self, ctx : Interpreter.Context) -> bool:
        dec = ctx.verb.declaration.lower()
        return any([dec=="5050",dec=="50",dec=="?"])

    def process(self, ctx : Interpreter.Context) -> Optional[str]:
        if ctx.verb.payload == None:
            return None
        result = random.choice(["", ctx.verb.payload])
        return result

