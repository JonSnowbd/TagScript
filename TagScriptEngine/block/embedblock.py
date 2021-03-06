from typing import Optional
import json
from .. import Interpreter
from ..interface import Block
from discord import Colour, Embed
from inspect import ismethod


class EmbedParseError(Exception):
    """Raised if an exception occurs while attempting to parse an embed."""


class BadColourArgument(EmbedParseError):
    """Exception raised when the colour is not valid."""

    def __init__(self, argument):
        self.argument = argument
        super().__init__(f'Colour "{argument}" is invalid.')


def string_to_color(argument: str):
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
    An embed block will send an embed in the tag response using properly formatted json.

    Usage: ``{embed(<json>)}``

    Payload: None

    Parameter: json

    Example::

        {embed({"title":"Hello!", "description":"This is a test embed."})}
    """

    ALLOWED_ATTRIBUTES = ("description", "embed", "color", "colour")

    def will_accept(self, ctx: Interpreter.Context) -> bool:
        dec = ctx.verb.declaration.lower()
        return dec == "embed"

    @staticmethod
    def get_embed(ctx: Interpreter.Context) -> Embed:
        return ctx.response.actions.get("embed", Embed())

    @staticmethod
    def text_to_embed(text: str) -> Embed:
        try:
            data = json.loads(text)
        except json.decoder.JSONDecodeError as error:
            raise EmbedParseError from error
        if data.get("embed"):
            data = data["embed"]
        if data.get("timestamp"):
            data["timestamp"] = data["timestamp"].strip("Z")
        try:
            embed = Embed.from_dict(data)
        except Exception as error:
            raise EmbedParseError from error
        else:
            return embed

    @staticmethod
    def update_embed(embed: Embed, attribute: str, value: str) -> Embed:
        if attribute in ("color", "colour"):
            value = string_to_color(value)
        setattr(embed, attribute, value)
        return embed

    def process(self, ctx: Interpreter.Context) -> Optional[str]:
        lowered = ctx.verb.parameter.lower()
        if not ctx.verb.parameter:
            embed = self.get_embed(ctx)
        elif ctx.verb.parameter.startswith("{") and ctx.verb.parameter.endswith("}"):
            try:
                embed = self.text_to_embed(ctx.verb.parameter)
            except EmbedParseError as error:
                return str(error)
        elif lowered in self.ALLOWED_ATTRIBUTES and ctx.verb.payload:
            embed = self.get_embed(ctx)
            try:
                embed = self.update_embed(embed, lowered, ctx.verb.payload)
            except EmbedParseError as error:
                return str(error)
        else:
            return

        try:
            length = len(embed)
        except Exception as error:
            return str(error)
        if length > 6000:
            return f"`MAX EMBED LENGTH REACHED ({length}/6000)`"
        ctx.response.actions["embed"] = embed
        return ""
