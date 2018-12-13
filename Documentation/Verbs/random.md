# Random Verb

The Random verb is used to have the interpreter pick a random value out of a preset list of objects. 

The verb can take an optional cast type to confirm types and also take an "Seed" value. The Seed value will make sure that random rolls will always pick the same value given that same Seed value.

This verb should be ambiguous and flexible regarding the delimiter.
Simple usage through `,` and advanced delimiting with `~`.

## FAQ

#### My output is split incorrectly
If you are using commas as part of actual grammar, you must instead use `~`
to separate all the possible choices.

#### Theres odd spacing in my random output
`{#:1, 2, 3} bottles on the wall` As you can see here, as it is in english,
there is a space after each comma. These are being interpreted as an actual
space that would appear in the output. Try to keep it tight where it makes
sense!

The correct version of the above is: `{#:1,2,3} bottles on the wall`

#### Aliases
The following will all work: 

`{#:1,2,3}`

`{random:1,2,3}`

`{rand:1,2,3}`

## Basics

`{random:Carl,Harold,Josh} attempts to pick the lock!`

Will boil down to a random name from that list, like this

`Josh attempts to pick the lock!`

## Advanced

`He picked up the {random(48):Cheese,Apple,Fork}`

The parameter describer after random denotes the Seed value. When the Seed
value is provided it will 'lock' the choice to be the same every time it is
given that same Seed value. if the Seed value of `48` is given we'll
see(purely an example)

`He picked up the Fork`

Running it again with `48` as the Seed value, we will yet again get 

`he picked up the Fork`

This is in place to provide easy logic to lock choices down to a per user basis.

For example, if we wanted a tag that assigned a user a deterministic classification we could do this

`{user} the {random({user}):Mage,Warrior,Hunter} attacks for {random:10,30,40,800!} damage`

Say Tony uses this.

`Tony the Mage attacks for 30 damage`

`Tony the Mage attacks for 40 damage`

`Tony the Mage attacks for 800! damage`

He's always a mage! The Seed is a valuable tool to have consistency in your randomness.