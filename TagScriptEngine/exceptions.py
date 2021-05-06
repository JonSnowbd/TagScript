__all__ = (
    "TagScriptError",
    "WorkloadExceededError",
    "ProcessError",
    "EmbedParseError",
    "BadColourArgument",
)

class TagScriptError(Exception):
    """Base class for all module errors."""


class WorkloadExceededError(TagScriptError):
    """Raised when the interpreter goes over its passed character limit."""


class ProcessError(TagScriptError):
    """
    Raised when an exception occurs during interpreter processing.
    
    Attributes
    ----------
    original: Exception
        The original exception that occurred during processing.
    """

    def __init__(self, error: Exception):
        self.original = error
        super().__init__(error)


class EmbedParseError(TagScriptError):
    """Raised if an exception occurs while attempting to parse an embed."""


class BadColourArgument(EmbedParseError):
    """
    Raised when the passed input fails to convert to `discord.Colour`.

    Attributes
    ----------
    argument: str
        The invalid input.
    """

    def __init__(self, argument: str):
        self.argument = argument
        super().__init__(f'Colour "{argument}" is invalid.')
