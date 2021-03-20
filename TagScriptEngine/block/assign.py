from .. import Interpreter, adapter
from ..interface import Block
from typing import Optional


class AssignmentBlock(Block):
    """
    Variables are useful for choosing a value and referencing it later in a tag.
    Variables can be referenced using brackets as any other block.

    **Usage:** ``{=(<name>):<value>}``

    **Aliases:** ``assign, let, var``

    **Payload:** value

    **Parameter:** name

    **Examples:** ::

        {=(prefix):!}
        The prefix here is `{prefix}`.
        # The prefix here is `!`.

        {assign(day):Monday}
        {if({day}==Wednesday):It's Wednesday my dudes!|The day is {day}.}
        # The day is Wednesday.
    """

    def will_accept(self, ctx: Interpreter.Context) -> bool:
        dec = ctx.verb.declaration.lower()
        return dec in ("=", "assign", "let", "var")

    def process(self, ctx: Interpreter.Context) -> Optional[str]:
        if ctx.verb.parameter is None:
            return None
        ctx.response.variables[ctx.verb.parameter] = adapter.StringAdapter(str(ctx.verb.payload))
        return ""
