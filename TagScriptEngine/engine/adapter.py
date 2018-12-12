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
        return self.string