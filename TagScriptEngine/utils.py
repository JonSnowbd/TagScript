import re

__all__ = ("escape_content",)

pattern = re.compile(r"(?<!\\)([{():|}])")


def _sub_match(match: re.Match) -> str:
    return "\\" + match.group(1)


def escape_content(string: str) -> str:
    """
    Escapes given input to avoid tampering with engine/block behavior.
    """
    if string is None:
        return
    return pattern.sub(_sub_match, string)
