from inspect import ismethod

from .. import Verb
from ..interface import Adapter


class SafeObjectAdapter(Adapter):
    def __init__(self, base):
        self.object = base

    def get_value(self, ctx: Verb) -> str:
        if ctx.parameter is None:
            return str(self.object)
        if ctx.parameter.startswith("_") or "." in ctx.parameter:
            return
        try:
            attribute = getattr(self.object, ctx.parameter)
        except AttributeError:
            return
        if ismethod(attribute):
            return
        if isinstance(attribute, float):
            attribute = int(attribute)
        return str(attribute)
