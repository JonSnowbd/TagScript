from .. import Verb


class Adapter(object):
    def __init__(self):
        pass

    def __repr__(self):
        return f"<{type(self).__qualname__} at {hex(id(self))}>"

    def get_value(self, ctx: Verb) -> str:
        return ""
