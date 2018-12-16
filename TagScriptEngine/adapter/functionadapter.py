from .. import Verb
from ..interface import Adapter
class FunctionAdapter(Adapter):
    def __init__(self, function_pointer):
        self.fn = function_pointer

    def get_value(self, ctx : Verb) -> str:
        return str(self.fn())