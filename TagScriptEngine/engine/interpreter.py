from typing import Tuple, List, Optional
from ..verb import parse

class Interpreter(object):
    def __init__(self):
        self.blocks = []

    def process(self, message : str) -> str:
        result = message
        blacklist = []
        while self.has_verb(result):
            coords = self.get_deepest(result)
            str_slice = result[coords[0]:coords[1]]
            verb_context = parse(str_slice)

            for b in self.blocks:
                check = b.will_accept(verb_context)
                if check != None and check == True:
                    splice_in = b.process(verb_context, result)
                    result = self.replace_coordinates(result, coords, splice_in)
                    break

        return result

    def get_deepest(self, message   : str,
                          blacklist : List[int] = None) -> Tuple[Optional[int], Optional[int]]: # I give up, pep 8 line limit.
        """
            get_deepest will find the next (deepest embedded) verb pair
            and return the coordinates that locate the slice of this verb.

            For example

            get_deepest("and i say {hello:world}") will return (10,22)

            Optionally, provided a blacklist of every coordinate you want to
            ignore, this will skip over coordinates that you no longer
            want this to pick up on.
        """
        start = None
        end = None
        for i, ch in enumerate(message):
            if blacklist is not None:
                if i in blacklist:
                    continue
            if ch == "{":
                start = i
            if ch == "}":
                end = i
                break
        return (start, end)

    def has_verb(self, message : str) -> bool:
        coord = self.get_deepest(message)
        if coord[0] == None or coord[1] == None:
            return False
        else:
            return True
            

    def replace_coordinates(self, message : str,
                                  coord   : Tuple[int, int],
                                  insert  : str) -> str:
        """
            replace_coordinates takes an original message, coordinates of the
            slice range, and the insert to replace the coordinates with.

            This method does not care about the length of the insert compared
            to the length of the coordinate slice.
            
            Example

            `replace_coordinates("hello", (0,1), "'A")` will return
            "'Allo"

            or

            `replace_coordinates("hello", (0,1), "Jel")` will return
            "Jelllo"
        """
        return message[0:coord[0]] + insert + message[coord[1]+1:]