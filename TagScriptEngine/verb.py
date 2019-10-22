from typing import Optional

class Verb(object):
    """
        A simple class that represents the verb string
        broken down into a clean format for consumption
    """
    def __init__(self, verb_string : str = None):
        self.declaration : Optional[str] = None
        self.parameter : Optional[str] = None
        self.payload : Optional[str] = None
        if verb_string == None:
            return

        parsed_string = verb_string.strip("{}")

        in_dec = False
        dec_start = 0
        for i, v in enumerate(parsed_string[:200]):
            if v == "(":
                in_dec = True
                dec_start = i
                self.declaration = parsed_string[:i]
            if v == ")" and in_dec:
                in_dec = False
                self.parameter = parsed_string[dec_start+1:i]
                if parsed_string[i+1] == ':':
                    self.payload = parsed_string[i+2:]
                break
        else:
            res = parsed_string.split(":", 1)
            if len(res) == 2:
                self.payload = res[1]
            self.declaration = res[0]

        

        # if ":" in parsed_string:
        #     self.payload = parsed_string.split(":", 1)[1]

        # dec = parsed_string.split(":", 1)[0]

        # if "(" in dec:
        #     split_params = dec.split("(", 1)
        #     param = split_params[1].strip(")")
        #     self.parameter = param
        #     self.declaration = split_params[0]
        #     return
        # else:
        #     self.declaration = dec
        #     return
    
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