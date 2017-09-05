import re
import random

REGEX = re.compile("#{(.+?)}") # This regex finds the whole #{random~list~thing}

class RandomFilter():
    def Pick(self, string):
        return random.choice(string.split('~'))

    def Process(self, engine, text):
        search = REGEX.search(text)
        value = text

        if search is None:
            return text # exit early if no need to random search.

        for block in REGEX.findall(value):

            #second_search = REGEX.search(block)
            #if second_search is not None:
            #    block = block.replace("#{" + second_search.group(0) + "}", self.Pick(second_search.group(0)))

            value = value.replace("#{"+block+"}",self.Pick(block))

        return value

