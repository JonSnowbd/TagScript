from typing import Optional

from .. import Interpreter, Verb, adapter
from ..interface import Block


class ShortCutRedirectBlock(Block):
    def __init__(self, var_name):
        self.redirect_name = var_name

    def will_accept(self, ctx: Interpreter.Context) -> bool:
        return ctx.verb.declaration.isdigit()

    def process(self, ctx: Interpreter.Context) -> Optional[str]:
        blank = Verb()
        blank.declaration = self.redirect_name
        blank.parameter = ctx.verb.declaration
        ctx.verb = blank
        return None
