## Terminology

Verbs consist of 2-3 parts. These are the names they will be referred to
going forward.

`{declaration(parameter):payload}`

Declaration is the calling card of the verb.This is the name of the verb to
be used.

parameters are optional variables to pass into the verb, there isn't anything
special about this segment, it is mostly just to separate options and special
cases from the user input. For example, to name a variable in variable
assignment.

Payloads are user input that will be operated on. This should not contain
option-specific data, but rather the data that will be acted on.

## Rules

Going forward with the design I want to be sure I remember rules that make
this more consistent to use, and easy to implement.

1. Verbs must have a max of 3 segmentations. `{declaration(parameter):payload}`
This is to make sure that they can be intelligently parsed without needing
to make assumptions because it limits it to two possibilities:
`{declaration:payload}` or `{declaration(parameter):payload}`.

2. Verbs must always state dependencies regarding order of execution, eg a
variable verb must have all the assignments completed before it evaluates
itself.

3. Formatting will be respected. Verbs can span across multiple lines
and the declaration is case insensitive.