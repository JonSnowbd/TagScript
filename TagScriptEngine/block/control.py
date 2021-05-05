from typing import Optional

from ..interface import Block
from ..interpreter import Context
from . import helper_parse_if, helper_parse_list_if, helper_split


def parse_into_output(payload, result):
    if result is None:
        return None
    try:
        output = helper_split(payload, False)
        if output != None and len(output) == 2:
            if result:
                return output[0]
            else:
                return output[1]
        else:
            if result:
                return payload
            else:
                return ""
    except:
        return None


class AnyBlock(Block):
    def will_accept(self, ctx: Context) -> bool:
        dec = ctx.verb.declaration.lower()
        return any([dec == "any", dec == "or"])

    def process(self, ctx: Context) -> Optional[str]:
        if ctx.verb.payload is None or ctx.verb.parameter is None:
            return None
        result = any(helper_parse_list_if(ctx.verb.parameter) or [])
        return parse_into_output(ctx.verb.payload, result)


class AllBlock(Block):
    def will_accept(self, ctx: Context) -> bool:
        dec = ctx.verb.declaration.lower()
        return any([dec == "all", dec == "and"])

    def process(self, ctx: Context) -> Optional[str]:
        if ctx.verb.payload is None or ctx.verb.parameter is None:
            return None
        result = all(helper_parse_list_if(ctx.verb.parameter) or [])
        return parse_into_output(ctx.verb.payload, result)


class IfBlock(Block):
    def will_accept(self, ctx: Context) -> bool:
        dec = ctx.verb.declaration.lower()
        return dec == "if"

    def process(self, ctx: Context) -> Optional[str]:
        if ctx.verb.payload is None or ctx.verb.parameter is None:
            return None
        result = helper_parse_if(ctx.verb.parameter)
        return parse_into_output(ctx.verb.payload, result)
