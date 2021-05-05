from typing import Optional

from ..interface import Block
from ..interpreter import Context
from . import helper_parse_if


class BreakBlock(Block):
    def will_accept(self, ctx: Context) -> bool:
        dec = ctx.verb.declaration.lower()
        return any([dec == "break", dec == "shortcircuit", dec == "short"])

    def process(self, ctx: Context) -> Optional[str]:
        if helper_parse_if(ctx.verb.parameter) == True:
            ctx.response.body = ctx.verb.payload if ctx.verb.payload != None else ""
        return ""
