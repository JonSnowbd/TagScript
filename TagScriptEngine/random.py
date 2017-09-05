from .engine import Filter
import re

REGEX = re.compile("#{(.+)}") # This regex finds the whole #{random~list~thing}

class RandomFilter(Filter):
    def Process(self, text):
        return REGEX.sub("x", text)