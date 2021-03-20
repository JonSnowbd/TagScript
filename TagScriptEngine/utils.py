import re

pattern = re.compile(r"(?<!\\)([\|\(\)\:])")

def _sub_match(match: re.Match) -> str:
    print(match)
    return "\\" + match.group(1)

def escape_content(string: str) -> str:
    """
    Escapes given input to avoid tampering with engine/block behavior.
    """
    return pattern.sub(_sub_match, string)
