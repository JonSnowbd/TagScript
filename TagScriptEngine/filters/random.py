import regex
import random
import numpy

REGEX = regex.compile(r"#(\w*){(([^{}]|(?R))*)}") # This regex finds the whole #{random~list~thing}
WEIGHTREGEX = regex.compile(r"\d+\|")

class Solve():
    def __init__(self, full, search, fix):
        pass

class RandomFilter():

    def Pick(self, string):
        """Pick takes a string and takes a random item out of the list,
        separated by ~ or , if there are no tildes"""
        if WEIGHTREGEX.search(string) is not None:
            return self.PickWeighted(string)

        if "~" in string:
            return random.choice(string.split('~'))
        return random.choice(string.split(','))

    def SplitIntoList(self, string):
        if "~" in string:
            List = string.split('~')
        else:
            List = string.split(',')

        return List

    def PickWeighted(self, string):
        """Pick takes a string and takes a random item out of the list,
        separated by ~ or , if there are no tildes, weighted by a x| prefix."""
        List = self.SplitIntoList(string)
        Weights = []

        # Go through the list. If it start with x| then add its value to Weights
        # Otherwise default to 1
        for ind, bit in enumerate(List):
            Weight = 1
            try:
                if "|" in bit:
                    Weight = int(bit.split('|', 1)[0])
                    List[ind] = bit[len(str(Weight))+1:]
            except:
                Weight = 1
            Weights.append(Weight)

        normalized = [float(i)/sum(Weights) for i in Weights]
        return numpy.random.choice(List, None, p=normalized)


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
            reuse_tag = ""

            while s is not None: # While there is something to solve
                article = s.group(2)
                reuse_tag = s.group(1)
                s = REGEX.search(article) # Search again
            
            if(reuse_tag == ""):
                modify_me = modify_me.replace( "#{"+article+"}", str(self.Pick( article )), 1 )
            else:
                items = self.SplitIntoList(article)
                engine.Add_Variable(reuse_tag, lambda: random.choice(items))
                modify_me = modify_me.replace("#"+reuse_tag+"{"+article+"}", "", 1)

            return modify_me

        while REGEX.search(output) is not None:
            output = solve(output)

        return output

