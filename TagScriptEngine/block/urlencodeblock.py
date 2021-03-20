from urllib.parse import quote, quote_plus

from .. import Interpreter
from ..interface import Block


class URLEncodeBlock(Block):
    """
    This block will encode a given string into a properly formatted url
    with non-url compliant characters replaced. Using ``+`` as the parameter
    will replace spaces with ``+`` rather than ``%20``.

    **Usage:** ``{urlencode(["+"]):<string>}``

    **Payload:** string

    **Parameter:** "+", None

    **Examples:** ::

        {urlencode:covid-19 sucks}
        # covid-19%20sucks

        {urlencode(+):im stuck at home writing docs}
        # im+stuck+at+home+writing+docs

        # the following tagscript can be used to search up tag blocks
        # assume {args} = "command block"
        <https://phen-cogs.readthedocs.io/en/latest/search.html?q={urlencode(+):{args}}&check_keywords=yes&area=default>
        # <https://phen-cogs.readthedocs.io/en/latest/search.html?q=command+block&check_keywords=yes&area=default>
    """

    def will_accept(self, ctx: Interpreter.Context):
        dec = ctx.verb.declaration.lower()
        return dec == "urlencode"

    def process(self, ctx: Interpreter.Context):
        if not ctx.verb.payload:
            return
        method = quote_plus if ctx.verb.parameter == "+" else quote
        return method(ctx.verb.payload)
