from random import choice

from discord import Guild, Member, TextChannel

from ..interface import Adapter
from ..utils import escape_content
from ..verb import Verb

__all__ = (
    "AttributeAdapter",
    "MemberAdapter",
    "ChannelAdapter",
    "GuildAdapter",
)


class AttributeAdapter(Adapter):
    def __init__(self, base):
        self.object = base
        self._attributes = {
            "id": base.id,
            "created_at": base.created_at,
            "timestamp": int(base.created_at.timestamp()),
            "name": getattr(base, "name", str(base)),
        }
        self._methods = {}
        self.update_attributes()
        self.update_methods()

    def __repr__(self):
        return f"<{type(self).__qualname__} object={repr(self.object)}>"

    def update_attributes(self):
        pass

    def update_methods(self):
        pass

    def get_value(self, ctx: Verb) -> str:
        should_escape = False

        if ctx.parameter is None:
            return_value = str(self.object)
        else:
            if attr := self._attributes.get(ctx.parameter):
                value = attr
            elif method := self._methods.get(ctx.parameter):
                value = method()
            else:
                return

            if isinstance(value, tuple):
                value, should_escape = value

            return_value = str(value) if value is not None else None

        return escape_content(return_value) if should_escape else return_value


class MemberAdapter(AttributeAdapter):
    """
    The ``{author}`` block with no parameters returns the tag invoker's full username
    and discriminator, but passing the attributes listed below to the block payload
    will return that attribute instead.

    **Aliases:** ``user``

    **Usage:** ``{author([attribute])``

    **Payload:** None

    **Parameter:** attribute, None

    **Attributes:**

    id
        The author's Discord ID.
    name
        The author's username.
    nick
        The author's nickname, if they have one, else their username.
    avatar
        A link to the author's avatar, which can be used in embeds.
    discriminator
        The author's discriminator.
    created_at
        The author's account creation date.
    timestamp
        The author's account creation date as a UTC timestamp.
    joined_at
        The date the author joined the server.
    mention
        A formatted text that pings the author.
    bot
        Whether or not the author is a bot.
    """

    def update_attributes(self):
        additional_attributes = {
            "color": self.object.color,
            "colour": self.object.color,
            "nick": self.object.display_name,
            "avatar": (self.object.avatar_url, False),
            "discriminator": self.object.discriminator,
            "joined_at": getattr(self.object, "joined_at", self.object.created_at),
            "mention": self.object.mention,
            "bot": self.object.bot,
        }
        self._attributes.update(additional_attributes)


class ChannelAdapter(AttributeAdapter):
    """
    The ``{channel}`` block with no parameters returns the channel's full name
    but passing the attributes listed below to the block payload
    will return that attribute instead.

    **Usage:** ``{channel([attribute])``

    **Payload:** None

    **Parameter:** attribute, None

    **Attributes:**

    id
        The channel's ID.
    name
        The channel's name.
    created_at
        The channel's creation date.
    timestamp
        The channel's creation date as a UTC timestamp.
    nsfw
        Whether the channel is nsfw.
    mention
        A formatted text that pings the channel.
    topic
        The channel's topic.
    """

    def update_attributes(self):
        if isinstance(self.object, TextChannel):
            additional_attributes = {
                "nsfw": self.object.nsfw,
                "mention": self.object.mention,
                "topic": self.object.topic or None,
            }
            self._attributes.update(additional_attributes)


class GuildAdapter(AttributeAdapter):
    """
    The ``{server}`` block with no parameters returns the server's name
    but passing the attributes listed below to the block payload
    will return that attribute instead.

    **Aliases:** ``guild``

    **Usage:** ``{server([attribute])``

    **Payload:** None

    **Parameter:** attribute, None

    **Attributes:**

    id
        The server's ID.
    name
        The server's name.
    icon
        A link to the server's icon, which can be used in embeds.
    created_at
        The server's creation date.
    timestamp
        The server's creation date as a UTC timestamp.
    member_count
        The server's member count.
    bots
        The number of bots in the server.
    humans
        The number of humans in the server.
    description
        The server's description if one is set, or "No description".
    random
        A random member from the server.
    """

    def update_attributes(self):
        guild = self.object
        bots = 0
        humans = 0
        for m in guild.members:
            if m.bot:
                bots += 1
            else:
                humans += 1
        additional_attributes = {
            "icon": (guild.icon_url, False),
            "member_count": guild.member_count,
            "bots": bots,
            "humans": humans,
            "description": guild.description or "No description.",
        }
        self._attributes.update(additional_attributes)

    def update_methods(self):
        additional_methods = {"random": self.random_member}
        self._methods.update(additional_methods)

    def random_member(self):
        return choice(self.object.members)
