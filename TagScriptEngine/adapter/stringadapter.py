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
            if "+" not in ctx.parameter:
                index = int(ctx.parameter) - 1
                splitter = " " if ctx.payload is None else ctx.payload
                return self.string.split(splitter)[index]
            else:
                index = int(ctx.parameter.replace("+", "")) - 1
                splitter = " " if ctx.payload is None else ctx.payload
                if ctx.parameter.startswith("+"):
                    return splitter.join(self.string.split(splitter)[:index+1])
                elif ctx.parameter.endswith("+"):
                    return splitter.join(self.string.split(splitter)[index:])
                else:
                    return self.string.split(splitter)[index]
        except:
            return self.string

    def return_value(self, string: str) -> str:
        return escape_content(string) if self.escape_content else string
