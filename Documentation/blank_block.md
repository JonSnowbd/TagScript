```
class Block(object):
    def __init__(self):
        pass

    def will_accept(self, ctx : InterpreterContext) -> Optional[bool]:
        return False

    def pre_process(self, ctx : InterpreterContext):
        return None

    def process(self, ctx : InterpreterContext) -> Optional[str]:
        return None

    def post_process(self, ctx : InterpreterContext):
        return None
```