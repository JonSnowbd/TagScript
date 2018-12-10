class Context(object):
    """
        A simple class that represents the verb string
        broken down into a clean format for consumption
    """
    def __init__(self, declaration=None, payload=None, parameter=None):
        self.declaration = declaration
        self.parameter = parameter
        self.payload = payload
    
    def __str__(self):
        if self.parameter == None:
            return "{%s:%s}" % (self.declaration, self.payload)
        else:
            return "{%s(%s):%s}" % (self.declaration,
                                    self.parameter,
                                    self.payload)

    def __repr__(self):
        return "<Context DCL='%s' PLD='%s' PRM='%s'>" % (self.declaration,
                                                         self.payload,
                                                         self.parameter)

def parse(verb_string : str) -> Context:
    """
        Takes a verb string and breaks it down into a Context for easier
        handling.

        Example inputs: `{random:word,list}` `{hello:world}`
        Note: try not to feed this anything but the exact verb string.

        TODO: OPTIMIZE THIS, theres no way this is the best way to do this.
    """
    final = Context()
    parsed_string = verb_string.strip("{").strip("}")

    if ":" in parsed_string:
        final.payload = parsed_string.split(":", 1)[1]

    dec = parsed_string.split(":", 1)[0]

    if "(" in dec:
        split_params = dec.split("(", 1)
        param = split_params[1].strip(")")
        final.parameter = param
        final.declaration = split_params[0]
        return final
    else:
        final.declaration = dec
        return final
