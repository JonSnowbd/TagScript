import json
from inspect import ismethod
from typing import Optional, Union

from discord import Colour, Embed

from ..exceptions import BadColourArgument, EmbedParseError
from ..interface import Block
from ..interpreter import Context


def string_to_color(argument: str) -> Colour:
    arg = argument.replace("0x", "").lower()

    if arg[0] == "#":
        arg = arg[1:]
    try:
        value = int(arg, base=16)
        if not (0 <= value <= 0xFFFFFF):
            raise BadColourArgument(arg)
        return Colour(value=value)
    except ValueError:
        arg = arg.replace(" ", "_")
        method = getattr(Colour, arg, None)
        if arg.startswith("from_") or method is None or not ismethod(method):
            raise BadColourArgument(arg)
        return method()


class EmbedBlock(Block):
    """
    An embed block will send an embed in the tag response.
    There are two ways to use the embed block, either by using properly
    formatted embed JSON from an embed generator or manually inputting
    the accepted embed attributes.

    **JSON**

    Using JSON to create an embed offers complete embed customization.
    Multiple embed generators are available online to visualize and generate
    embed JSON.

    **Usage:** ``{embed(<json>)}``

    **Payload:** None

    **Parameter:** json

    **Examples:** ::

        {embed({"title":"Hello!", "description":"This is a test embed."})}
        {embed({
            "title":"Here's a random duck!",
            "image":{"url":"https://random-d.uk/api/randomimg"},
            "color":15194415
        })}

    **Manual**

    The following embed attributes can be set manually:
    *   ``title``
    *   ``description``
    *   ``color``

    **Usage:** ``{embed(<attribute>):<value>}``

    **Payload:** value

    **Parameter:** attribute

    **Examples:** ::

        {embed(color):#37b2cb}
        {embed(title):Support Guide}
        {embed(description):i like pizza}

    Both methods can be combined to create an embed in a tag.
    The following tagscript uses JSON to create an embed with fields and later
    set the embed title.

    ::

        {embed({{"fields":[{"name":"Field 1","value":"field description","inline":false}]})}
        {embed(title):my embed title}
    """

    ALLOWED_ATTRIBUTES = ("description", "title", "color", "colour")

    def will_accept(self, ctx: Context) -> bool:
        dec = ctx.verb.declaration.lower()
        return dec == "embed"

    @staticmethod
    def get_embed(ctx: Context) -> Embed:
        return ctx.response.actions.get("embed", Embed())

    @staticmethod
    def value_to_color(value: Optional[Union[int, str]]) -> Colour:
        if value is None or isinstance(value, Colour):
            return value
        if isinstance(value, int):
            return Colour(value)
        elif isinstance(value, str):
            return string_to_color(value)
        else:
            raise EmbedParseError("Received invalid type for color key (expected string or int)")

    def text_to_embed(self, text: str) -> Embed:
        try:
            data = json.loads(text)
        except json.decoder.JSONDecodeError as error:
            raise EmbedParseError(error) from error

        if data.get("embed"):
            data = data["embed"]
        if data.get("timestamp"):
            data["timestamp"] = data["timestamp"].strip("Z")

        color = data.pop("color", data.pop("colour", None))

        try:
            embed = Embed.from_dict(data)
        except Exception as error:
            raise EmbedParseError(error) from error
        else:
            if color := self.value_to_color(color):
                embed.color = color
            return embed

    @staticmethod
    def update_embed(embed: Embed, attribute: str, value: str) -> Embed:
        if attribute in ("color", "colour"):
            value = string_to_color(value)
        setattr(embed, attribute, value)
        return embed

    @staticmethod
    def return_error(error: Exception) -> str:
        return f"Embed Parse Error: {error}"

    @staticmethod
    def return_embed(ctx: Context, embed: Embed) -> str:
        try:
            length = len(embed)
        except Exception as error:
            return str(error)
        if length > 6000:
            return f"`MAX EMBED LENGTH REACHED ({length}/6000)`"
        ctx.response.actions["embed"] = embed
        return ""

    def process(self, ctx: Context) -> Optional[str]:
        if not ctx.verb.parameter:
            return self.return_embed(ctx, self.get_embed(ctx))

        lowered = ctx.verb.parameter.lower()
        try:
            if ctx.verb.parameter.startswith("{") and ctx.verb.parameter.endswith("}"):
                    embed = self.text_to_embed(ctx.verb.parameter)
            elif lowered in self.ALLOWED_ATTRIBUTES and ctx.verb.payload:
                embed = self.get_embed(ctx)
                embed = self.update_embed(embed, lowered, ctx.verb.payload)
            else:
                return
        except EmbedParseError as error:
            return self.return_error(error)

        return self.return_embed(ctx, embed)
