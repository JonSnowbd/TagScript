import regex
import random

REGEX = regex.compile(r"\?{([^{}]|(?R))*}") # This regex finds the whole #{random~list~thing}

class OptionalFilter():
    def Pick(self, string):
        """Returns either the string or nothing"""
        return random.choice(["", string])

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
                if article[0:2] == "?{":
                    article = article[2:]
                s = REGEX.search(article) # Search again

            modify_me = modify_me.replace( "?{"+article+"}", self.Pick( article ), 1 )
            return modify_me

        while REGEX.search(output) is not None:
            output = solve(output)

        return output

