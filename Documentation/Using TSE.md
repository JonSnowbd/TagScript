# Welcome to TSE v2

## Beginners

Lets learn this new system together by creating a few tags. Lets jump straight
in with a simple tag called `damage`. Lets make it so that when a user uses it
carl-bot will announce how much damage they take and how much they have left.

Later on we will be improving this tag to have more and more features. But for
now lets dive in a little.

```
!tag + damage {assign(damage):{range:1-49}}
You have 50hp! You take {damage} damage leaving you with {math:50-{damage}}
```

Woah thats a lot to start with! Lets take it from the top!

To begin with we use `{assign(damage):{range:1-49}}` to `assign` `{range:1-49}`
to a variable name we can access later, called `damage`, this is because if
we used `{range:1-49}` more than once, it will generate a different number
each time! and that would be incorrect.

And `{range:1-49}` itself is a verb that will generate a number between those
two numbers, make sure you dont forget the : or the -

With that assigned, we can now use the variable name inbetween 2 braces to get
that variable and use it. Typing out `{damage}` will be replaced with the number
that was generated and stored to `damage` earlier.

So, with that we use a `{math:50-{damage}}` block to calculate how much HP is
left after the hit! Of course this has no real impact on any variable or scenario, its
just a simple and fun little tag.

## Beginners 2

Lets slow down a little and work on the basics. Say you want something random in
your tag, be it a choice or a number between x and y, well its very simple. Lets
make a tag that lets the user ask the bot something and get a random response!

```
!tag + will {random:Yeah! Totally!~Nah, I definitely don't think so.~Hmm. Its close but nope}
```

See how easy that was? Now users can invoke this with `!will I live to see Dark Souls
4?` and the bot will of course reply with `Nah, I definitely don't think so.`

In a random verb, you separate the choices with `~`, but, if you're not going to
use `,` for grammatical purposes, youre free to use `,` instead! though note
I don't recommend this as it can be volatile if you forget that `,` are splitters
and not a pause in the sentence.

## Explore!

There are many tags currently in TSE and lots more to come!

Check them all out in these community tags to import into your own servers

**todo, just released :(**