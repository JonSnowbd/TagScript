from .. import verb

class Adapter(object):
    def __init__(self):
        pass

    def get_value(self, ctx : verb.VerbContext) -> str:
        return ""

class StringAdapter(Adapter):
    def __init__(self, string : str):
        self.string : str = string

    def get_value(self, ctx : verb.VerbContext) -> str:
        if ctx.parameter == None:
            return self.string
        try:
            if ":" not in ctx.parameter:
                index = int(ctx.parameter) - 1
                splitter = " " if ctx.payload == None else ctx.payload
                return self.string.split(splitter)[index]
        except:
            return self.string

class IntAdapter(Adapter):
    def __init__(self, integer : int):
        self.integer : int = integer

    def get_value(self, ctx : verb.VerbContext) -> str:
        return str(self.integer)