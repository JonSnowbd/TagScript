# Features

## CheatSheet

| Syntax | Feature | Usage |
|----------------------------|------------------------------------------------------------------------------------------------|---------------------------|
| !{variable1=My Giant Dong} | Assigns variable for re use. Anything after the = is the variable. Spaces will not be trimmed. | boi look at my $variable1 |
| #{one~two~three} apples | Chooses a variable from the provided list, each member is separated by ~ or | | N/A |

## Random selection blocks**

`I am #{angery~happy~mad} today.`

These are blocks that are evaluated to a random member of the list, this list is NOT separated by commas as they are used extensively in english grammar.

Instead separate each member of the list with either of the following characters `~ |`

## Variable Assignment

```
!{person1= Carl}

I really #{hate~love} $person1 since #{he~she} is so sexy. I'm jealous of $person1.
```

Variable names must be all lowercase and can only contain letters and numbers.

you can assign a variable that can be reused. This feature is important due for various reasons regarding other features. for example if you randomly generate a conversation between 2 people, you cannot #{steve, bob, parker} for each time they are mentioned, you need to remember which person is which, as shown below.

```
!{person1= #{Carl~Nith~Yenni~Kintark}}
!{person2= #{Yenni~Nith~Kintark~Carl}}

$person1 called over $person2 for a quick chat about the weather.
$person2 looks over and compliments $person1's shoes.
```

If you randomly generated each mention it would not make sense.

>Carl called over Yenni for a quick chat about the weather.
Kintark looks over and compliments Nith's shoes.

Variables fix this and let you reuse a random choice in a way that makes sense.

>Carl called over Yenni for a quick chat about the weather.
Yenni looks over and compliments Carl's shoes.

## API

Using TagScript is easy, instantiate `TagScriptEngine.Engine()`, then inject any variable you need into it with `e.Add_Variable("author", "name")`
`e.Clear_Variables()` or inject your own dictionary as the lookup for variables with 
```
new_dictionary = {"author":"name","user":"name"}
e.Set_Variables(new_dictionary)
```

Then you can process tags with `e.Process("#{tag~text}")`

A full example is as such:

```
from TagScriptEngine import Engine

x = Engine()
x.Add_Variable("author", "pysnow")

print(x.Process("boy $author sure is #{awful~amazing}"))
```