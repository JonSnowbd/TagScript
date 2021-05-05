from itertools import islice
from typing import Any, Dict, List, Optional, Tuple

from .exceptions import ProcessError, TagScriptError, WorkloadExceededError
from .interface import Block, Adapter
from .verb import Verb

__all__ = (
    "Node",
    "build_node_tree",
    "Response",
    "Context",
    "Interpreter",
)


class Node:
    def __init__(self, coordinates: Tuple[int, int], ver: Verb = None):
        self.output: Optional[str] = None
        self.verb: Verb = ver
        self.coordinates: Tuple[int, int] = coordinates

    def __str__(self):
        return str(self.verb) + " at " + str(self.coordinates)

    def __repr__(self):
        return "<Node verb={0.verb!r} coordinates={0.coordinates!r}>".format(self)


def build_node_tree(message: str) -> List[Node]:
    """
    build_node_tree will take a message and get every possible match
    """
    nodes = []
    previous = r""

    starts = []
    for i, ch in enumerate(message):
        if ch == "{" and previous != r"\\":
            starts.append(i)
        if ch == "}" and previous != r"\\":
            if not starts:
                continue
            coords = (starts.pop(), i)
            n = Node(coords)
            nodes.append(n)

        previous = ch
    return nodes


class Response:
    """
    Response is another packaged class that contains data
    relevent only to the current process, and should not leak out
    into interpretation on other tags. This is also what is handed
    after a finished response.

    :attr:`actions` is a dict of recommended actions to take with the
    response. Think of these as headers in HTTP.

    :attr:`variables` is a dict intended to be shared between all the
    blocks. For example if a variable is shared here, any block going
    forward can look for it.

    :attr:`body` is the finished, cleaned message with all verbs
    interpreted.
    """

    def __init__(self):
        self.body: str = None
        self.actions: Dict[str, Any] = {}
        self.variables: Dict[str, Adapter] = {}

    def __repr__(self):
        return "<Response body={0.body!r} actions={0.actions!r} variables={0.variables!r}>".format(
            self
        )


class Context:
    """
    Context is a simple packaged class that makes it
    convenient to make Blocks have a small method signature.

    :attr:`verb` will be the verbs context, has all 3 parts of a verb,
    payload(the main data), the declaration(the name its calling) and
    the parameter(settings and modifiers)

    :attr:`original_message` will contain the entire message before
    it was edited. This is convenient for various post and pre
    processes.

    :attr:`interpreter` is the reference to the `Interpreter` object
    that is currently handling the process. Use this reference to get
    and store variables that need to persist across processes. useful
    for caching heavy calculations.
    """

    def __init__(self, verb: Verb, res: Response, interpreter, og: str):
        self.verb: Verb = verb
        self.original_message: str = og
        self.interpreter = interpreter
        self.response: Response = res

    def __repr__(self):
        return "<Context verb={0.verb!r}>".format(self)


class Interpreter:
    """
    The TagScript interpreter.

    Should be initialized with a list of :ref:`Block` to use when processing tagscript.
    """

    def __init__(self, blocks: List[Block]):
        self.blocks: List[Block] = blocks

    def __repr__(self):
        return "<Interpreter blocks={0.blocks!r}>".format(self)

    def _get_acceptors(self, ctx: Context, node: Node):
        acceptors: List[Block] = [b for b in self.blocks if b.will_accept(ctx)]
        for b in acceptors:
            value = b.process(ctx)
            if value is not None:  # Value found? We're done here.
                node.output = value
                break

    def _solve(
        self, message: str, node_ordered_list: List[Node], response: Response, charlimit: int, *, verb_limit: int = 2000
    ):
        final = message
        total_work = 0

        for i, node in enumerate(node_ordered_list):
            # Get the updated verb string from coordinates and make the context
            node.verb = Verb(
                final[node.coordinates[0] : node.coordinates[1] + 1], limit=verb_limit
            )
            ctx = Context(node.verb, response, self, message)

            # Get all blocks that will attempt to take this
            self._get_acceptors(ctx, node)
            if node.output is None:
                continue  # If there was no value output, no need to text deform.

            if charlimit is not None:
                total_work = total_work + len(
                    node.output
                )  # Record how much we've done so far, for the rate limit
                if total_work > charlimit:
                    raise WorkloadExceededError(
                        "The TSE interpreter had its workload exceeded. The total characters "
                        f"attempted were {total_work}/{charlimit}"
                    )

            start, end = node.coordinates
            message_slice_len = (end + 1) - start
            replacement_len = len(node.output)
            differential = (
                replacement_len - message_slice_len
            )  # The change in size of `final` after the change is applied
            if "TSE_STOP" in response.actions:
                return final[:start] + node.output
            final = final[:start] + node.output + final[end + 1 :]

            # if each coordinate is later than `start` then it needs the diff applied.
            for future_n in islice(node_ordered_list, i + 1, None):
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

        return final

    def process(
        self, message: str, seed_variables: Dict[str, Adapter] = None, charlimit: Optional[int] = None
    ) -> Response:
        """Processes a given TagScript string.

        Parameters
        -----------
        message: :class:`str`
            A TagScript string to be processed.
        seed_variables: Dict[str, Any]
            A dictionary containing strings to adapters to provide context variables for processing.
        charlimit: int
            The maximum characters to process.

        Raises
        -------
        :exc:`WorkloadExceededError`
            Signifies the interpreter reached the character limit, if one was provided.

        Returns
        --------
        :class:`Response`
            A response object containing the proccessed body, actions and variables.
        """
        response = Response()
        message_input = message

        # Apply variables fed into `process`
        if seed_variables is not None:
            response.variables = {**response.variables, **seed_variables}

        node_ordered_list = build_node_tree(message_input)

        try:
            output = self._solve(message_input, node_ordered_list, response, charlimit)
        except TagScriptError:
            raise
        except Exception as error:
            raise ProcessError(error) from error

        # Dont override an overridden response.
        if response.body is None:
            response.body = output.strip("\n ")
        else:
            response.body = response.body.strip("\n ")
        return response
