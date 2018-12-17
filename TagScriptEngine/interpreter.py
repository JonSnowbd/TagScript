from typing import Tuple, List, Optional, Dict, Any, Set
from . import Verb
from .interface import Block
from itertools import islice

def build_node_tree(message : str) -> List['Interpreter.Node']:
    """
        build_node_tree will take a message and get every possible match
    """
    nodes = []
    previous = r""

    starts = []
    for i, ch in enumerate(message):
        if ch == "{" and previous != r'\\':
            starts.append(i)
        if ch == "}" and previous != r'\\':
            if len(starts) == 0:
                continue
            coords = (starts.pop(), i)
            n = Interpreter.Node(coords)
            nodes.append(n)

        previous = ch
    return nodes

class Interpreter(object):
    def __init__(self, blocks : List[Block]):
        self.blocks : List[Block] = blocks

    class Node(object):
        def __init__(self, coordinates : Tuple[int,int], ver : Verb = None):
            self.output : Optional[str] = None
            self.verb : Verb = ver
            self.coordinates : Tuple[int,int] = coordinates
        
        def __str__(self):
            return str(self.verb)+" at "+str(self.coordinates)

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
        """
        def __init__(self, verb : Verb, res : 'Interpreter.Response', inter : 'Interpreter', og : str):
            self.verb : Verb = verb
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
            from .interface import Adapter
            self.body : str = None
            self.actions : Dict[str, Any] = {}
            self.variables : Dict[str, Adapter] = {}

    def process(self, message : str, seed_variables : Dict[str, Any] = None) -> 'Interpreter.Response':
        response = Interpreter.Response()

        # Apply variables fed into `process`
        if seed_variables is not None:
            response.variables = {**response.variables, **seed_variables}

        node_ordered_list = build_node_tree(message)

        final = message

        for i, n in enumerate(node_ordered_list):
            # Get the updated verb string from coordinates and make the context
            n.verb = Verb(final[n.coordinates[0]:n.coordinates[1]+1])
            ctx = Interpreter.Context(n.verb, response, self, message)

            # Get all blocks that will attempt to take this
            acceptors : List[Block] = [b for b in self.blocks if b.will_accept(ctx)]
            for b in acceptors:
                value = b.process(ctx)
                if value != None: # Value found? We're done here.
                    n.output = value
                    break

            if n.output == None:
                continue # If there was no value output, no need to text deform.

            start, end = n.coordinates
            message_slice_len = (end+1) - start
            replacement_len = len(n.output)
            differential = replacement_len - message_slice_len # The change in size of `final` after the change is applied
            final = final[:start]+n.output+final[end+1:]
            
            # if each coordinate is later than `start` then it needs the diff applied.
            for future_n in islice(node_ordered_list, i+1, None):
                new_start = None
                new_end = None
                if future_n.coordinates[0] > start:
                    new_start = future_n.coordinates[0] + differential
                else:
                    new_start = future_n.coordinates[0]
                    
                if future_n.coordinates[1] > start:
                    new_end = future_n.coordinates[1] + differential
                else:
                    new_end = future_n.coordinates[1]
                future_n.coordinates = (new_start, new_end)
        # Dont override an overridden response.
        if response.body == None:
            response.body = final.strip("\n ")
        else:
            response.body = response.body.strip("\n ")
        return response