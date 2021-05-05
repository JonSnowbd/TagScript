from ..interface import Adapter
from ..verb import Verb


class FunctionAdapter(Adapter):
    def __init__(self, function_pointer):
        self.fn = function_pointer

    def __repr__(self):
        return f"<{type(self).__qualname__} fn={repr(self.fn)}>"

    def get_value(self, ctx: Verb) -> str:
        return str(self.fn())
