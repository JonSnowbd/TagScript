from .. import Interpreter, adapter
from ..interface import Block
from typing import Optional
import random, math

class RangeBlock(Block):
    def will_accept(self, ctx : Interpreter.Context) -> bool:
        dec = ctx.verb.declaration.lower()
        return any([dec=="rangef",dec=="range"])

    def process(self, ctx : Interpreter.Context) -> Optional[str]:
        try:
            spl = ctx.verb.payload.split("-")
            random.seed(ctx.verb.parameter)
            if ctx.verb.declaration.lower() == "rangef":
                lower = float(spl[0])
                upper = float(spl[1])
                base = random.randint(lower*10,upper*10) / 10
                return str(base)
                # base = random.randint(lower, upper)
                # if base == upper:
                #     return str(base)
                # if ctx.verb.parameter != None:
                #     random.seed(ctx.verb.parameter+"float")
                # else:
                #     random.seed(None)
                # return str(str(base)+"."+str(random.randint(1,9)))
            else:
                lower = int(float(spl[0]))
                upper = int(float(spl[1]))
                return str(random.randint(lower, upper))
        except:
            return None

