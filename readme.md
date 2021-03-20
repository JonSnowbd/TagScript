## Information

This repository is a fork of JonSnowbd's [TagScript](https://github.com/JonSnowbd/TagScript).
This fork adds support for Discord object adapters and a couple Discord related blocks, as 
well as multiple utility blocks. Additionally, several tweaks have been made to the engine's 
behavior.

This TagScriptEngine is used on [Noumenon, a Discord bot](https://discordapp.com/oauth2/authorize?client_id=634866217764651009&permissions=2080894207&scope=bot%20applications.commands). 
An example implementation can be found its [Tags cog](https://github.com/phenom4n4n/phen-cogs/tree/master/tags),
which also includes [documentation on the blocks found here](https://phen-cogs.readthedocs.io/en/latest/?badge=latest).

## Installation

Download the latest version through pip:

```
pip(3) install git+https://github.com/phenom4n4n/TagScript.git
```

Download from a commit:

```
pip(3) install git+https://github.com/phenom4n4n/TagScript.git@<COMMIT_HASH>
```

Install for editing/development:

```
git clone https://github.com/phenom4n4n/TagScript.git
pip(3) install -e ./TagScript
```

## What?

TagScript is a drop in easy to use string interpreter that lets you provide users with ways of
customizing their profiles or chat rooms with interactive text.

For example TagScript comes out of the box with a random block that would let users provide
a template that produces a new result each time its ran, or assign math and variables for later
use. See [the documentation folder](https://github.com/JonSnowbd/TagScript/tree/v2/Documentation) for
some design documents and basic tutorials or hit up our [biggest user's documentation](https://docs.carl.gg/tags-and-triggers/tags-advanced-usage/) to see how its being used
on one of the biggest bots on discord!

## Dependencies

`Python 3.5+` due to type hinting

`PyParsing` provides the math block with intelligent mathematical expressions

`appJar` is required if one wants to use the playground feature
