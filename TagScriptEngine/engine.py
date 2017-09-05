from .random import RandomFilter

class Filter():
    """This is the base class for filters to extend."""
    def Process(self, text):
        """Process should take text and return the string with the filter's effect"""
        return text


class Engine():
    """Engine is the core of this library, it is what you will instantiate to process text script."""
    def __init__(self):
        self.variable_bin = {}
        self.filters = []

        self.filters.append(RandomFilter())

    def Process(self, text):
        value = text

        for f in self.filters: # Apply each filter
            value = f.Process(value)

        return value