from .. import Verb
from ..interface import Adapter


class IntAdapter(Adapter):
    def __init__(self, integer: int):
        self.integer: int = integer

    def get_value(self, ctx: Verb) -> str:
        return str(self.integer)
