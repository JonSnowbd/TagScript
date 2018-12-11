class Response(object):
    def __init__(self):
        self.Actions = {}
        self.Body = ""

    def add_action(self, action_name : str,
                         action_variable,
                         overwrite : bool = True):
        """
            add_action takes `action_name` as a key, and `action_variable`
            as a value. Optional parameter overwrite will determine if
            the action should be overwritten if it already exists.

            We recommend using the constant strings provided by
            `TagScriptEngine.action` to assign action_names to avoid mishaps
            with spelling mistakes and to help with intellisense. 
        """
        if self.Actions[action_name] is not None:
            if overwrite == False:
                return
        self.Actions[action_name] = action_variable