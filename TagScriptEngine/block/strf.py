from .. import engine
from . import Block
from typing import Optional
import datetime

class StrfBlock(Block):
    def will_accept(self, ctx : engine.Interpreter.Context) -> bool:
        return ctx.verb.declaration == "strf"

    def process(self, ctx : engine.Interpreter.Context) -> Optional[str]:
        if ctx.verb.parameter:
            if ctx.verb.parameter.isdigit():
                try:
                    t = datetime.datetime.fromtimestamp(int(ctx.verb.parameter))
                except:
                    return None
            else:
                try:
                    t = datetime.datetime.strptime(ctx.verb.parameter, '%Y-%m-%d %H.%M.%S')
                except ValueError:
                    return None
        else:
            t = datetime.datetime.utcnow()
        if ctx.verb.payload is not None:
            result = t.strftime(ctx.verb.payload)
            ctx.handled = True
            return result
        else:
            return None
