## Beginners

Lets slow down a little and work on the basics. Say you want something random in
your tag, be it a choice or a number between x and y, well its very simple. Lets
make a tag that lets the user ask the bot something and get a random response!

```
{random:Yeah! Totally!~Nah, I definitely don't think so.~Hmm. Its close but nope}
```

See how easy that was? Now users can invoke this with `!will I live to see Dark Souls
4?` and the bot will of course reply with `Nah, I definitely don't think so.`

In a random verb, you separate the choices with `~`, but, if you're not going to
use `,` for grammatical purposes, youre free to use `,` instead! though note
I don't recommend this as it can be volatile if you forget that `,` are splitters
and not a pause in the sentence.