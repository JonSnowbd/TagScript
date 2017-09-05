from .random import RandomFilter
from .variable import VariableFilter


class Engine():
    """Engine is the core of this library, it is what you will instantiate to process text script."""
    def __init__(self):
        self.variable_bin = {}

        self.random = RandomFilter()
        self.var = VariableFilter()

    def Set_Variables(self, vars):
        self.variable_bin = vars

    def Clear_Variables(self):
        self.variable_bin = {}

    def Add_Variable(self, name, val):
        self.variable_bin[name] = val

    def Process(self, text):
        value = text

        value = self.random.Process(self, value)
        value = self.var.Process(self, value)

        return value