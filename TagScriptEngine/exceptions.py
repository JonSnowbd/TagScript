class TagScriptError(Exception):
    """Base class for all module errors."""


class WorkloadExceededError(TagScriptError):
    """Raised when the interpreter goes over its passed character limit."""


class ProcessError(TagScriptError):
    """Raised when an exception occurs during interpreter processing."""

    def __init__(self, error: Exception):
        self.original = error
        super().__init__(error)


class EmbedParseError(TagScriptError):
    """Raised if an exception occurs while attempting to parse an embed."""


class BadColourArgument(EmbedParseError):
    """Exception raised when the colour is not valid."""

    def __init__(self, argument):
        self.argument = argument
        super().__init__(f'Colour "{argument}" is invalid.')
