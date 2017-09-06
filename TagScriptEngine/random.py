import re
import random

REGEX = re.compile("#{(.+[^}])}") # This regex finds the whole #{random~list~thing}

class Solve():
    def __init__(self, full, search, fix):
        pass

class RandomFilter():
    def Pick(self, string):

        if "~" in string:
            return random.choice(string.split('~'))

        return random.choice(string.split(','))

    def Process(self, engine, text):
        search = REGEX.search(text)
        value = text
        Has_Randoms = True # A safeguard for breaking the while

        if search is None:
            Has_Randoms = False
            return text # exit early if no need to search.

        match = REGEX.search(value)

        while Has_Randoms:

            if match is None: #No more matches, exit out
                Has_Randoms = False
                break

            internal = REGEX.search(match.group(1)) #Search inside the capture for another #{}

            if internal is not None:
                match = internal # If it has one, set it up as the new match.
                continue # and restart.

            value = value.replace( match.group(0), self.Pick(match.group(1)).strip("#{").strip("}") )
            match = REGEX.search(value) # Restart the process

        return value

