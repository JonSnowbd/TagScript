from typing import Optional


class Verb(object):
    """
    A simple class that represents the verb string
    broken down into a clean format for consumption
    """

    def __init__(self, verb_string: str = None):
        self.declaration: Optional[str] = None
        self.parameter: Optional[str] = None
        self.payload: Optional[str] = None
        if verb_string is None:
            return

        parsed_string = verb_string[1:-1]

        dec_depth = 0
        dec_start = 0

        for i, v in enumerate(parsed_string[:2000]):
            if v == ":" and not dec_depth:
                res = parsed_string.split(":", 1)
                if len(res) == 2:
                    self.payload = res[1]
                self.declaration = res[0]
                return
            elif v == "(":
                dec_depth += 1
                if not dec_start:
                    dec_start = i
                    self.declaration = parsed_string[:i]
            elif v == ")" and dec_depth:
                dec_depth -= 1
                if dec_depth == 0:
                    self.parameter = parsed_string[dec_start + 1 : i]
                    try:
                        if parsed_string[i + 1] == ":":
                            self.payload = parsed_string[i + 2 :]
                    except IndexError:
                        pass
                    return
        else:
            res = parsed_string.split(":", 1)
            if len(res) == 2:
                self.payload = res[1]
            self.declaration = res[0]

    def __str__(self):
        """This makes Verb compatible with str(x)"""
        response = "{"
        if self.declaration != None:
            response += self.declaration
        if self.parameter != None:
            response += "(" + self.parameter + ")"
        if self.payload != None:
            response += ":" + self.payload
        return response + "}"

    def __repr__(self):
        return "<Verb DCL='%s' PLD='%s' PRM='%s'>" % (
            self.declaration,
            self.payload,
            self.parameter,
        )
