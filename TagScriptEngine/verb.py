from typing import Optional


class Verb:
    """
    A simple class that represents the verb string
    broken down into a clean format for consumption
    """

    def __init__(self, verb_string: str = None, *, limit: int = 2000):
        self.declaration: Optional[str] = None
        self.parameter: Optional[str] = None
        self.payload: Optional[str] = None
        if verb_string is None:
            return

        self.parsed_string = verb_string[1:-1]

        self.dec_depth = 0
        self.dec_start = 0
        self.skip_next = False

        for i, v in enumerate(self.parsed_string[:limit]):
            if self.skip_next:
                self.skip_next = False
                continue
            elif v == "\\":
                print(i, v)
                self.skip_next = True
            elif v == ":" and not self.dec_depth:
            # if v == ":" and not dec_depth:
                self.set_payload()
                return
            elif v == "(":
                self.open_parameter(i)
            elif v == ")" and self.dec_depth:
                if self.close_parameter(i):
                    return
        else:
            self.set_payload()

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

    def set_payload(self):
        res = self.parsed_string.split(":", 1)
        if len(res) == 2:
            self.payload = res[1]
        self.declaration = res[0]

    def open_parameter(self, i: int):
        self.dec_depth += 1
        if not self.dec_start:
            self.dec_start = i
            self.declaration = self.parsed_string[:i]

    def close_parameter(self, i: int) -> bool:
        self.dec_depth -= 1
        if self.dec_depth == 0:
            self.parameter = self.parsed_string[self.dec_start + 1 : i]
            try:
                if self.parsed_string[i + 1] == ":":
                    self.payload = self.parsed_string[i + 2 :]
            except IndexError:
                pass
            return True
        return False
