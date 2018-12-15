# Assign Verb

Assign is your way of assigning a value to a name for reuse across your entire
tag.

## FAQ

#### Aliases

The following all work:

`{=(varname):Content}`

`{assign(varname):Content}`

`{let(varname):Content}`

`{var(varname):Content}`

## Basic Usage

The text inside the brackets is the identifier for the text beyond the `:`. This
means that if you `{assign(big):A very large snake approaches you.}` you can now
use `{big}` and TSE will replace it with `A very large snake approaches you.`
automatically.