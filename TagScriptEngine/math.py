import re, ast

REGEX = re.compile("[mM]{(.+[^}])}")

class MathEvaluationFilter():
    def Process(self, engine, text):
        value = text

        match = REGEX.search(value)
        if match is None:
            return value # Exit early if there is no math expressions to begin with

        while match is not None:
            evaluation = ast.literal_eval(match.group(1))
            value = value.replace(match.group(0), str(evaluation))
            match = REGEX.search(value)

        return value