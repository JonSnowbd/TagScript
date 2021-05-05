from typing import Optional

from ..adapter import StringAdapter
from ..interface import Block
from ..interpreter import Context


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
        # The day is Monday.
    """

    def will_accept(self, ctx: Context) -> bool:
        dec = ctx.verb.declaration.lower()
        return dec in ("=", "assign", "let", "var")

    def process(self, ctx: Context) -> Optional[str]:
        if ctx.verb.parameter is None:
            return None
        ctx.response.variables[ctx.verb.parameter] = StringAdapter(str(ctx.verb.payload))
        return ""
