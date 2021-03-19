import re

SPLIT_REGEX = re.compile(r"(?<!\\)\|")

def helper_parse_if(if_string: str):
    """
    Parses the if_string manually to test for equality between its
    members.

    >>> helper_parse_if("this == this")
    True
    >>> helper_parse_if("2>3")
    False
    >>> helper_parse_if("40 >= 40")
    True
    """
    try:
        if "!=" in if_string:
            spl = if_string.split("!=")
            return spl[0].strip() != spl[1].strip()
        if "==" in if_string:
            spl = if_string.split("==")
            return spl[0].strip() == spl[1].strip()
        if ">=" in if_string:
            spl = if_string.split(">=")
            return float(spl[0].strip()) >= float(spl[1].strip())
        if "<=" in if_string:
            spl = if_string.split("<=")
            return float(spl[0].strip()) <= float(spl[1].strip())
        if ">" in if_string:
            spl = if_string.split(">")
            return float(spl[0].strip()) > float(spl[1].strip())
        if "<" in if_string:
            spl = if_string.split("<")
            return float(spl[0].strip()) < float(spl[1].strip())
    except:
        return None
    return None


def helper_split(split_string: str, easy: bool = True):
    """
    A helper method to universalize the splitting logic used in multiple
    blocks and adapters. Please use this wherever a verb needs content to
    be chopped at | , or ~!

    >>> helper_split("this, should|work")
    ["this, should", "work"]
    """
    if "|" in split_string:
        return SPLIT_REGEX.split(split_string)
    if easy and "~" in split_string:
        return split_string.split("~")
    if easy and "," in split_string:
        return split_string.split(",")
    return None


def helper_parse_list_if(if_string):
    split = helper_split(if_string, False)
    if split is None:
        return [helper_parse_if(if_string)]
    return [helper_parse_if(item) for item in split]
