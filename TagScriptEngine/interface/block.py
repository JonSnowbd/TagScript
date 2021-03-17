from typing import Optional


class Block(object):
    """
    WIP DOCS

    **Usage:** ``{block(<parameter>):[payload]}``

    **Aliases:** ``alias, alias``

    **Payload:** None

    **Parameter:** None

    **Examples:** ::

        {block}
    """

    def __init__(self):
        pass

    def __repr__(self):
        return f"<{type(self).__qualname__} at {hex(id(self))}>"

    def will_accept(self, ctx: "Interpreter.Context") -> Optional[bool]:
        return False

    def pre_process(self, ctx: "Interpreter.Context"):
        return None

    def process(self, ctx: "Interpreter.Context") -> Optional[str]:
        return None

    def post_process(self, ctx: "Interpreter.Context"):
        return None
