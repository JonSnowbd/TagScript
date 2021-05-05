import datetime
from typing import Optional

from ..interface import Block
from ..interpreter import Context


class StrfBlock(Block):
    def will_accept(self, ctx: Context) -> bool:
        return ctx.verb.declaration == "strf"

    def process(self, ctx: Context) -> Optional[str]:
        if ctx.verb.parameter:
            if ctx.verb.parameter.isdigit():
                try:
                    t = datetime.datetime.fromtimestamp(int(ctx.verb.parameter))
                except:
                    return None
            else:
                try:
                    t = datetime.datetime.strptime(ctx.verb.parameter, "%Y-%m-%d %H.%M.%S")
                except ValueError:
                    return None
        else:
            t = datetime.datetime.utcnow()
        if ctx.verb.payload is not None:
            return t.strftime(ctx.verb.payload)
        else:
            return None
