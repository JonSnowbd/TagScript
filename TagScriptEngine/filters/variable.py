import re

ASSIGNMENT_REGEX = re.compile(r"!{(.+)=(.+)}") # Regex to find assignment blocks.
INTERP_REGEX = re.compile(r"\$(\w+)([;=]?)")

class VariableFilter():
    def __init__(self):
        pass

    def Process(self, engine, text):
        value = text
        variable_block = engine.variable_bin

        # register and delete each !{assignment=variable}
        for (name, val) in ASSIGNMENT_REGEX.findall(value):
            variable_block[name] = val
            value = value.replace("!{"+name+"="+val+"}", '').strip("\n").strip(' ')

        if INTERP_REGEX.search(value) is None:
            return value

        # Replace each $var with its variable block value.
        for (varname, modifier) in INTERP_REGEX.findall(value):
            if varname in variable_block:
                value = value.replace("$"+varname, variable_block[varname])
            elif "=" in modifier: # Substitution required.
                substitute = modifier.strip("=")
                value = value.replace("$"+varname+modifier, substitute)
            elif ";" in modifier: # remove null optional variables
                value = value.replace("$"+varname+modifier, "")

        return value