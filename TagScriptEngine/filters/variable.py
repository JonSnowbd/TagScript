import re

ASSIGNMENT_REGEX = re.compile(r"!{(.+)=(.+)}") # Regex to find assignment blocks.
INTERP_REGEX = re.compile(r"\$(\w+)(=?\w*)")

class VariableFilter():
    def __init__(self):
        pass

    def Process(self, engine, text):
        value = text
        variable_block = engine.variable_bin

        matches = INTERP_REGEX.findall(value)
        if matches is None:
            return value
        # Replace any $vars inside of an assignment block with their corresponding value
        for (varname, modifier) in matches: 
            if varname in variable_block:
                value = value.replace("$"+varname+modifier, variable_block[varname])

        # register and delete each !{assignment=variable}
        for (name, val) in ASSIGNMENT_REGEX.findall(value):
            variable_block[name] = val
            value = value.replace("!{"+name+"="+val+"}", '').strip("\n").strip(' ')

        # Replace each $var with its variable block value.
        for (varname, modifier) in INTERP_REGEX.findall(value): 
            if varname in variable_block:
                value = value.replace("$"+varname+modifier, variable_block[varname])
            elif "=" in modifier: # Substitution required.
                substitute = modifier.strip("=")
                value = value.replace("$"+varname+modifier, substitute)
                    
        return value