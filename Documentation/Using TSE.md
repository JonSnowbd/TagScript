# Welcome to TSE v2

## Here for Carlbot specific TSE? Please use the website to edit/make tags!

The experience of adding and editing tags will be much less limited on the
[official carlbot website, carl.gg!](https://carl.gg/)

Anyway, here's the rundown of each article:

- [**Assign**](https://github.com/JonSnowbd/TagScript/blob/v2/Documentation/Verbs/assign.md)
use assign to place content into something you can reuse. Pro tip variables
will evaluate into something that can be used by other variables eg
`{assign(start):thisis}{assign(thisistorb):TORBJORN} Okay, {{start}torb}`

- [**Random**](https://github.com/JonSnowbd/TagScript/blob/v2/Documentation/Verbs/random.md)
use random when you want a random choice between lots of things.

- [**Range**](https://github.com/JonSnowbd/TagScript/blob/v2/Documentation/Verbs/range.md)
use range when you want to get a number between 2 numbers(and including those 2
numbers).

- [**Meta tags**](https://github.com/JonSnowbd/TagScript/blob/v2/Documentation/Verbs/meta.md)
use these assortment of meta tags to alter how carlbot responds to each

- [**Math tags**](https://github.com/JonSnowbd/TagScript/blob/v2/Documentation/Verbs/math.md)
use these to calculate anything you need

- [**Carlbot specific Variables**](https://github.com/JonSnowbd/TagScript/blob/v2/Documentation/carlbot.md)

## Tutorials

- [**Beginners v1**](https://github.com/JonSnowbd/TagScript/blob/v2/Documentation/Beginners_1.md)

- [**Beginners v2**](https://github.com/JonSnowbd/TagScript/blob/v2/Documentation/Beginners_2.md)

With more to come soon for our advanced users! For now though if you want to learn
more please see the initial section to see the advanced features of each verb
we have!

## Explore!

There are many tags currently in TSE and lots more to come!

Check them all out in these community tags to import into your own servers, and
see the power of TSE v2!

**Carl's RPG Sim!**

Defeat the strongest of runescape monsters!
```
{let(enemy):{random:Ice troll,Fire giant,Abyssal demon}}
{let(damage):{range:1-10}}
{let(damagetwo):{range:5-15}}
{let(hp):{random({enemy}):10,20,40}}
{let(hptwo):{math:{hp}-({damagetwo} + {damage})}}
{user(proper)} attacks {enemy} for {damage} damage. The enemy now has {math:{hp}-{damage}}/{hp}hp
{user(proper)} swings a second time and deals {damagetwo} damage. The enemy has {hptwo} hp. {if({hptwo}<0): EZCLAP | I lagged}
```

**Play A Scuffed Lotto by PySnow!**

*I know this isnt how lotto works but it looks nicer :(*

    {let(s1):{range(part1{server(id)}{strf:%b%Y}):10-99}}
    {let(s2):{range(part2{server(id)}{strf:%b%Y}):10-99}}
    {let(s3):{range(part3{server(id)}{strf:%b%Y}):10-99}}
    {let(s4):{range(part4{server(id)}{strf:%b%Y}):10-99}}
    {let(s5):{range(part5{server(id)}{strf:%b%Y}):10-99}}
    {let(sp):{range(partp{server(id)}{strf:%b%Y}):100-999}}

    {let(p1):{range(part1{user(id)}{strf:%b%Y}):10-99}}
    {let(p2):{range(part2{user(id)}{strf:%b%Y}):10-99}}
    {let(p3):{range(part3{user(id)}{strf:%b%Y}):10-99}}
    {let(p4):{range(part4{user(id)}{strf:%b%Y}):10-99}}
    {let(p5):{range(part5{user(id)}{strf:%b%Y}):10-99}}
    {let(pp):{range(partp{user(id)}{strf:%b%Y}):100-999}}

    {random:Hey everybody! Lets draw the numbers~Hey there! Here are your numbers~Whoo!~Heeeeereeee weeee go!}
    ```diff
    - House
    - {s1} {s2} {s3} {s4} {s5} PB: {sp}
    + You
    + {p1} {p2} {p3} {p4} {p5} PB: {pp}
    ```
    Thanks for {random:participating~playing~joining us~trying}, **{user(proper)}**!!