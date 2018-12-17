from .. import Interpreter, adapter
from . import helper_parse_if
from ..interface import Block
from typing import Optional
import random

class BreakBlock(Block):
    def will_accept(self, ctx : Interpreter.Context) -> bool:
        dec = ctx.verb.declaration.lower()
        return any([dec=="break",dec=="shortcircuit",dec=="short"])

    def process(self, ctx : Interpreter.Context) -> Optional[str]:
        if helper_parse_if(ctx.verb.parameter) == True:
            ctx.response.body = ctx.verb.payload if ctx.verb.payload != None else ""
        return ""

