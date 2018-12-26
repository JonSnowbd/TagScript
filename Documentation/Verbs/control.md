# Control blocks

There are 4 basic ways to control the flow of your tag. This is advanced stuff
so don't try to tackle this until you're comfortable with TSE!

Before I can rapidly explain each tag, I must explain one thing they have in common:

Each tag will take conditionals in their parentheses like so `{if(1==1):hello}`
in these parenthesis you can use the following operators

- `==` Checks if the two are the exact same
- `!=` Checks if the two are different in any way
- `>` and `>=` checks if the number on the left side is larger than the one on the right
- `<` and `<=` checks if the number on the left side is smaller than the one on the right

Now, with that out of the way here are the control blocks

    {if(1==1):I will show!|Never reached}
    {any(1==1|2==3|5==10):I will show!}
    {break(1==3):This is all the message will be if its true}
    {all(1==1|2==2|3==3):if all of those are true, this will show|and if not, this will.}

So, as you can see the result can be separated with | to have an else in them.

Break is special; if the condition in `break`'s parentheses is true, then the
entire output will solely be the payload.

NEW: Stop is a new addition to TSE. Use it to halt a tag then and there if the
expression in its parenthesis is true.