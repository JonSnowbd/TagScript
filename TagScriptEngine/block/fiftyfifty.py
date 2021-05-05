import random
from typing import Optional

from ..interface import Block
from ..interpreter import Context


class FiftyFiftyBlock(Block):
    def will_accept(self, ctx: Context) -> bool:
        dec = ctx.verb.declaration.lower()
        return any([dec == "5050", dec == "50", dec == "?"])

    def process(self, ctx: Context) -> Optional[str]:
        if ctx.verb.payload is None:
            return None
        return random.choice(["", ctx.verb.payload])
