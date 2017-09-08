# TagScriptEngine

A fast simple and easy way to get dynamic text templates. Intended to be used as a (third party)user input template engine,
generally used in discord bots for things that require more flexibility than something like `text.replace("thing", "something better")`
could possibly give you.

With TagScriptEngine users can give you dynamic templates such as
```
Today is going to be a #{good,bad,iffy,horrible} day.
```
That when invoked through TagScriptEngine, will output the string with the #{} block reduced to a random from
the list provided.

There is much more to TSE at the moment including but not limited to

* Variable assignment (from users and from serverside)
* Math evaluation blocks
* Random choice blocks
* Variable substitution

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing

```
pip install TagScriptEngine
```

#### Development

A step by step series of examples that tell you how to get a development env running

First you should clone the repository

```
git clone git@github.com:JonSnowbd/TagScript.git
```

Install the dependencies

```
pip install -R requirements.txt
pip install -R dev_requirements.txt
```

Then you are free to develop and change whatever you like.

## Running the tests

Running tests for TagScriptEngine is easy and intuitive, with nose2 installed you
can run all the tests by opening a console and going into the base directory and running:
```
nose2
```

## Built With

* [PyParsing](https://sourceforge.net/projects/pyparsing/) - A great parsing library that made it easy to develop 
