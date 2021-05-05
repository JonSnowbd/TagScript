from typing import Optional

from ..interface import Block
from ..interpreter import Context
from ..verb import Verb


class ShortCutRedirectBlock(Block):
    def __init__(self, var_name):
        self.redirect_name = var_name

    def will_accept(self, ctx: Context) -> bool:
        return ctx.verb.declaration.isdigit()

    def process(self, ctx: Context) -> Optional[str]:
        blank = Verb()
        blank.declaration = self.redirect_name
        blank.parameter = ctx.verb.declaration
        ctx.verb = blank
        return None
