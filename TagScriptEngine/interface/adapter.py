from typing import Optional


class Adapter:
    def __init__(self):
        pass

    def __repr__(self):
        return f"<{type(self).__qualname__} at {hex(id(self))}>"

    def get_value(self, ctx: "interpreter.Context") -> Optional[str]:
        return ""
