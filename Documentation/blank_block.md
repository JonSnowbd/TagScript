Here is a simple copy paste block to be used in your stack.

The rundown is simple; `will_accept` should return a bool indicating whether
or not the block is interested in handling the verb. The most common way is
to just check the verb's `declaration`.

`process` should take the context and return the value that should be calculated.
Like how a math block will take the `payload` of the verb and return the result
of the calculation.

Don't forget to set `ctx.handled` to be True if you are not returning None

```
from TagScriptEngine import engine, block
from typing import Optional

class GenericBlock(block.Block):
    def will_accept(self, ctx : engine.Interpreter.Context) -> bool:
        return ctx.verb.declaration == "generic"

    def process(self, ctx : engine.Interpreter.Context) -> Optional[str]:
        ctx.handled = True
        return "It worked"
```