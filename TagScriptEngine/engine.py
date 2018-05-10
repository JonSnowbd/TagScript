from .filters import RandomFilter, VariableFilter, MathEvaluationFilter, OptionalFilter, STRFFilter, ScriptFilter
import discord

class Engine():
    """Engine is the core of this library, it is what you will instantiate to process text script"""
    def __init__(self):
        self.variable_bin = {}

        self.random = RandomFilter()
        self.var = VariableFilter()
        self.math = MathEvaluationFilter()
        self.optional = OptionalFilter()
        self.strf = STRFFilter()
        self.script = ScriptFilter()

    def Set_Variables(self, variable_dict : dict):
        """Overrides every variable"""
        self.variable_bin = variable_dict
        return self

    def Clear_Variables(self):
        """Clears every variable"""
        self.variable_bin = {}
        return self

    def Add_Variable(self, name : str, value : any):
        """Adds a single variable with name and value"""
        self.variable_bin[name] = value
        return self

    def Add_Variables(self, variable_dict : dict):
        """Merges the provided variable_dict into the variable bin"""
        self.variable_bin = {**self.variable_bin, **variable_dict}

    def Process(self, text : str, message : discord.Message = None):
        value = text

        value = self.strf.Process(self, value)
        value = self.optional.Process(self, value) # Then optionalities
        value = self.random.Process(self, value) # Clear out randoms first
        value = self.var.Process(self, value) # Then change out $Variables
        value = self.math.Process(self, value) # Finally math can work with those gone.
        
        if self.script.IsScript(value):
            return self.script.Process(self, value, message)

        return value
