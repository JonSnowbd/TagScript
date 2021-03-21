from .. import Verb
from ..interface import Adapter
from ..utils import escape_content


class StringAdapter(Adapter):
    def __init__(self, string: str, *, escape: bool = False):
        self.string: str = str(string)
        self.escape_content = escape

    def __repr__(self):
        return f"<{type(self).__qualname__} string={repr(self.string)}>"

    def get_value(self, ctx: Verb) -> str:
        return self.return_value(self.handle_ctx(ctx))

    def handle_ctx(self, ctx: Verb) -> str:
        if ctx.parameter is None:
            return self.string
        try:
            splitter = " " if ctx.payload is None else ctx.payload
            split = self.string.split(splitter)
            if "+" not in ctx.parameter:
                index = int(ctx.parameter) - 1
                return split[index]
            else:
                index = int(ctx.parameter.replace("+", "")) - 1
                joined = splitter.join(split)
                if ctx.parameter.startswith("+"):
                    return joined[: index + 1]
                elif ctx.parameter.endswith("+"):
                    return joined[index:]
                else:
                    return split[index]
        except:
            return self.string

    def return_value(self, string: str) -> str:
        return escape_content(string) if self.escape_content else string
