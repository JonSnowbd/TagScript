from typing import Optional

from ..interface import Block
from ..interpreter import Context


class RedirectBlock(Block):
    """
    Redirects the tag response to either the given channel, the author's DMs,
    or uses a reply based on what is passed to the parameter.

    **Usage:** ``{redirect(<"dm"|"reply"|channel>)}``

    **Payload:** None

    **Parameter:** "dm", "reply", channel

    **Examples:** ::

        {redirect(dm)}
        {redirect(reply)}
        {redirect(#general)}
        {redirect(626861902521434160)}
    """

    def will_accept(self, ctx: Context) -> bool:
        dec = ctx.verb.declaration.lower()
        return dec == "redirect"

    def process(self, ctx: Context) -> Optional[str]:
        if not ctx.verb.parameter:
            return None
        param = ctx.verb.parameter.strip()
        if param.lower() == "dm":
            target = "dm"
        elif param.lower() == "reply":
            target = "reply"
        else:
            target = param
        ctx.response.actions["target"] = target
        return ""
