from .. import Interpreter, adapter
from . import helper_parse_if
from ..interface import Block
from typing import Optional


class StopBlock(Block):
    """
    The stop block stops tag processing if the given parameter is true. If a
    message is passed to the payload it will return that message.

    **Usage:** ``{stop(<bool>):[string]}``

    **Aliases:** ``halt, error``

    **Payload:** bool

    **Parameter:** string, None

    **Example:** ::

        {stop({args}==):You must provide arguments for this tag.}
        # enforces providing arguments for a tag
    """

    def will_accept(self, ctx: Interpreter.Context) -> bool:
        dec = ctx.verb.declaration.lower()
        return dec in ("stop", "halt", "error")

    def process(self, ctx: Interpreter.Context) -> Optional[str]:
        if ctx.verb.parameter is None:
            return None
        if helper_parse_if(ctx.verb.parameter):
            ctx.response.actions["TSE_STOP"] = True
            return "" if ctx.verb.payload is None else ctx.verb.payload
        return ""
