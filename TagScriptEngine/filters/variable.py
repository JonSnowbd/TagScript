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

        # Once to clear out vars in nested random assignment blocks... bit hacky
        for (varname, modifier) in INTERP_REGEX.findall(value): 
            if varname in variable_block:
                sub = variable_block[varname]
                if callable(sub):
                    value = value.replace("$"+varname+modifier, sub(), 1)
                else:
                    value = value.replace("$"+varname+modifier, sub)
                
            elif "=" in modifier: # Substitution required.
                substitute = modifier.strip("=")
                value = value.replace("$"+varname+modifier, substitute)

        # register and delete each !{assignment=variable}
        for (name, val) in ASSIGNMENT_REGEX.findall(value):
            variable_block[name] = val
            value = value.replace("!{"+name+"="+val+"}", '').strip("\n").strip(' ')

        # Once to clear out vars in nested random assignment blocks... bit hacky
        for (varname, modifier) in INTERP_REGEX.findall(value): 
            if varname in variable_block:
                sub = variable_block[varname]
                if callable(sub):
                    value = value.replace("$"+varname+modifier, sub(), 1)
                else:
                    value = value.replace("$"+varname+modifier, sub)
                
            elif "=" in modifier: # Substitution required.
                substitute = modifier.strip("=")
                value = value.replace("$"+varname+modifier, substitute)
                    
        return value