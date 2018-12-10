# Meta verbs

These verbs have no real impact on the end result of the message but instead
focus on changing how carlbot reacts!

### silent

{silent} will make the outcome completely silent. The output will never be
sent. This is useful for muting the output of a command alias.

### react

{react:😂} will make carlbot add a reaction to his own message. If this is
not acceptable and you'd rather he reacted to the message that triggered it
then you may add a parameter to the verb like so {react(user):😂}

Adding multiple emoji to the reaction is simple: {react:😂😭💯} with no need
to space it out or comma separate. That said given how discord emoji
selectors work, you can space it out if that is more convenient.

This would look like `{react: :joy: :sob: :100: }` and it would parse
correctly.