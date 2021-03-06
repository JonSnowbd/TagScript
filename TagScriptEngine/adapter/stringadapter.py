from .. import Verb
from ..interface import Adapter


class StringAdapter(Adapter):
    def __init__(self, string: str):
        self.string: str = string

    def get_value(self, ctx: Verb) -> str:
        if ctx.parameter == None:
            return self.string
        try:
            if "+" not in ctx.parameter:
                index = int(ctx.parameter) - 1
                splitter = " " if ctx.payload == None else ctx.payload
                return self.string.split(splitter)[index]
            else:
                index = int(ctx.parameter.replace("+", "")) - 1
                splitter = " " if ctx.payload == None else ctx.payload
                if ctx.parameter.startswith("+"):
                    return splitter.join(self.string.split(splitter)[: index + 1])
                elif ctx.parameter.endswith("+"):
                    return splitter.join(self.string.split(splitter)[index:])
                else:
                    return self.string.split(splitter)[index]
        except:
            return self.string
