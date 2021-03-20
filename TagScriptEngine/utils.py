import re

SPLITTER_REGEX = re.compile(r"(?<!\\)\|")


def escape_content(string: str) -> str:
    """
    Escapes given input to avoid tampering with engine/block behavior.
    """
    return SPLITTER_REGEX.sub(r"\|", string)
