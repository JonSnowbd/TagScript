from .. import Interpreter
from ..interface import Block


class ReplaceBlock(Block):
    def will_accept(self, ctx: Interpreter.Context):
        dec = ctx.verb.declaration.lower()
        return dec == "replace"

    def process(self, ctx: Interpreter.Context):
        if not ctx.verb.parameter or not ctx.verb.payload:
            return
        try:
            before, after = ctx.verb.parameter.split(",", 1)
        except ValueError:
            return

        return ctx.verb.payload.replace(before, after)


class PythonBlock(Block):
    def will_accept(self, ctx: Interpreter.Context):
        dec = ctx.verb.declaration.lower()
        return dec in ("contains", "in", "index")

    def process(self, ctx: Interpreter.Context):
        dec = ctx.verb.declaration.lower()
        if dec == "contains":
            return str(bool(ctx.verb.parameter in ctx.verb.payload.split())).lower()
        elif dec == "in":
            return str(bool(ctx.verb.parameter in ctx.verb.payload)).lower()
        else:
            try:
                return str(ctx.verb.payload.strip().split().index(ctx.verb.parameter))
            except ValueError:
                return "-1"
