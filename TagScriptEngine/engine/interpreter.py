from typing import Tuple, List, Optional, Dict, Any
from ..verb import parse, VerbContext

class Interpreter(object):
    def __init__(self, blocks):
        self.blocks = blocks

    class Context(object):
        """
            Interpreter.Context is a simple packaged class that makes it
            convenient to make Blocks have a small method signature.

            `self.verb` will be the verbs context, has all 3 parts of a verb,
            payload(the main data), the declaration(the name its calling) and
            the parameter(settings and modifiers)

            `self.original_message` will contain the entire message before
            it was edited. This is convenient for various post and pre
            processes.

            `self.interpreter` is the reference to the `Interpreter` object
            that is currently handling the process. Use this reference to get
            and store variables that need to persist across processes. useful
            for caching heavy calculations.

            `
        """
        def __init__(self, vc : 'VerbContext', res : 'Interpreter.Response', inter : 'Interpreter', og : str):
            self.verb : 'VerbContext' = vc
            self.original_message : str = og
            self.interpreter : 'Interpreter' = inter
            self.response : 'Interpreter.Response' = res


    class Response(object):
        """
            Interpreter.Response is another packaged class that contains data
            relevent only to the current process, and should not leak out
            into interpretation on other tags. This is also what is handed
            after a finished response.

            `self.actions` is a dict of recommended actions to take with the
            response. Think of these as headers in HTTP.

            `self.variables` is a dict intended to be shared between all the
            blocks. For example if a variable is shared here, any block going
            forward can look for it.

            `self.body` is the finished, cleaned message with all verbs
            interpreted.
        """
        def __init__(self):
            self.body : str = None
            self.actions : Dict[str, Any] = {}
            self.variables : Dict[str, Any] = {}
            self.error : bool = False
            self.error_message : Optional[str] = None


    def process(self, message : str, seed_variables : Dict[str, Any] = None) -> 'Interpreter.Response':
        result = message
        response = Interpreter.Response()
        blacklist = []
        try:
            while self.has_verb(result):
                coords = self.get_deepest(result, blacklist)
                str_slice = result[coords[0]:coords[1]]

                # Package everything into a context for easy use.
                ctx = Interpreter.Context(parse(str_slice), response, self, message)

                acceptors = [b for b in self.blocks if b.will_accept(ctx)]

                if len(acceptors) < 1:
                    blacklist.append(coords[0])
                    blacklist.append(coords[1])
                    continue

                # Provide preprocessing
                for b in acceptors:
                    b.pre_process(ctx)

                # Mutate result
                for b in acceptors:
                    splice_in = b.process(ctx)
                    result = self.replace_coordinates(result, coords, splice_in)
                    break

                # Provide postprocessing
                for b in acceptors:
                    b.post_process(ctx)
        except Exception as E:
            response.error = True
            response.error_message = str(E)
            
        response.body = result
        return response

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