from .. import Interpreter, adapter
from . import helper_parse_if
from ..interface import Block
from typing import Optional
import random

class StopBlock(Block):
    def will_accept(self, ctx : Interpreter.Context) -> bool:
        dec = ctx.verb.declaration.lower()
        return any([dec=="stop",dec=="halt"])

    def process(self, ctx : Interpreter.Context) -> Optional[str]:
        if ctx.verb.parameter == None:
            return None
        if helper_parse_if(ctx.verb.parameter):
            ctx.response.actions["TSE_STOP"] = True
            return "" if ctx.verb.payload == None else ctx.verb.payload
        return ""

