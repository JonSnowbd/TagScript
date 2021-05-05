from typing import Optional

from ..interpreter import Context


class Adapter:
    def __init__(self):
        pass

    def __repr__(self):
        return f"<{type(self).__qualname__} at {hex(id(self))}>"

    def get_value(self, ctx: Context) -> Optional[str]:
        return ""
