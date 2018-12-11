from ..verb import Context
from . import Block
from typing import Optional
import random

class RandomBlock(Block):
    def will_accept(self, verb_context : Context) -> bool:
        return verb_context.declaration == "random"

    def process(self, verb_context : Context, entire_string : str) -> Optional[str]:
        spl = verb_context.payload.split("~")
        if verb_context.parameter is not None:
            random.seed(verb_context.parameter)
        return random.choice(spl)
