from typing import Optional

class Verb(object):
    """
        A simple class that represents the verb string
        broken down into a clean format for consumption
    """
    def __init__(self, verb_string : str):
        self.declaration : Optional[str] = None
        self.parameter : Optional[str] = None
        self.payload : Optional[str] = None

        parsed_string = verb_string
        if parsed_string[-1] == "}":
            parsed_string = parsed_string[:-1]
        if parsed_string[0] == "{":
            parsed_string = parsed_string[1:]

        if ":" in parsed_string:
            self.payload = parsed_string.split(":", 1)[1]

        dec = parsed_string.split(":", 1)[0]

        if "(" in dec:
            split_params = dec.split("(", 1)
            param = split_params[1].strip(")")
            self.parameter = param
            self.declaration = split_params[0]
            return
        else:
            self.declaration = dec
            return
    
    def __str__(self):
        "This makes Verb compatible with str(x)"
        response = "{"
        if self.declaration != None:
            response += self.declaration
        if self.parameter != None:
            response += "("+self.parameter+")"
        if self.payload != None:
            response += ":"+self.payload
        return response + "}"

    def __repr__(self):
        return "<Verb DCL='%s' PLD='%s' PRM='%s'>" % (self.declaration,
                                                         self.payload,
                                                         self.parameter)