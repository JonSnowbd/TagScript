from ..verb import Context
from typing import Optional

class Block(object):
    def __init__(self):
        pass

    def will_accept(self, verb_context : Context) -> Optional[bool]:
        return False

    def pre_process(self, verb_context : Context, entire_string : str):
        return None

    def process(self, verb_context : Context, entire_string : str) -> Optional[str]:
        return None

    def post_process(self, verb_context : Context, entire_string : str):
        return None