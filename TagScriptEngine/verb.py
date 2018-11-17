class VerbContext(object):
    def __init__(self, declaration=None, payload=None, parameter=None):
        self.declaration = declaration
        self.parameter = parameter
        self.payload = payload

async def Parse_Verb(user_string : str) -> VerbContext:
    """
    Takes a verb string and breaks it down into a VerbContext for easier handling.
    Example inputs: `{random:word,list}` `{hello:world}`
    Note: try not to feed this anything but the verb string.
    """
    parsed_string = user_string.strip("{").strip("}")

    # Get the declaration by splitting at the first colon.
    declaration = parsed_string.split(':', 1)[0]
    payload = parsed_string.split(":", 1)[1]


    return VerbContext(declaration, payload)
