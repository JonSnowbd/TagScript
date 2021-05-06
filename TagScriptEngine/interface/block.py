from typing import Optional


class Block:
    """
    The base class for TagScript blocks.

    Implementations must subclass this to create new blocks.
    """

    def __init__(self):
        pass

    def __repr__(self):
        return f"<{type(self).__qualname__} at {hex(id(self))}>"

    def will_accept(self, ctx: "interpreter.Context") -> Optional[bool]:
        """
        Describes whether the block is valid for the given `Context`.

        Subclasses must implement this.

        Parameters
        ----------
        ctx: Context
            The context object containing the TagScript `Verb`.

        Returns
        -------
        bool
            Whether the block should be processed for this `Context`.

        Raises
        ------
        NotImplementedError
            The subclass did not implement this required method.
        """
        raise NotImplementedError

    def pre_process(self, ctx: "interpreter.Context"):
        return None

    def process(self, ctx: "interpreter.Context") -> Optional[str]:
        return None

    def post_process(self, ctx: "interpreter.Context"):
        return None
