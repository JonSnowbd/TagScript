import regex
import random

REGEX = regex.compile("#{([^{}]|(?R))*}") # This regex finds the whole #{random~list~thing}

class Solve():
    def __init__(self, full, search, fix):
        pass

class RandomFilter():
    def Pick(self, string):
        """Pick takes a string and takes a random item out of the list,
        separated by ~ or , if there are no tildes"""
        if "~" in string:
            return random.choice(string.split('~'))
        return random.choice(string.split(','))

    def Process(self, engine, text):   
        output = text
        # Early exit check
        search = REGEX.search(output)
        if search is None:
            return output # exit early if no need to search.

        def solve(modify_me):
            """Sub function to iterate over the string and
            dive as deep as it can into a search, solve it and retry."""
            s = REGEX.search(modify_me)
            if s is None:
                return modify_me
            article = ""
            while s is not None: # While there is something to solve
                article = s.group(0)
                if article[-1] == "}":
                    article = article[:-1]
                if article[0:2] == "#{":
                    article = article[2:]
                s = REGEX.search(article) # Search again

            modify_me = modify_me.replace( "#{"+article+"}", self.Pick( article ), 1 )
            return modify_me

        while REGEX.search(output) is not None:
            output = solve(output)

        return output

