import pyparsing, ast

INTEGER = pyparsing.Word(pyparsing.nums)

EXPOP = pyparsing.Literal('^')
SIGNOP = pyparsing.oneOf('+ -')
MULTOP = pyparsing.oneOf('* /')
PLUSOP = pyparsing.oneOf('+ -')
FACTOP = pyparsing.Literal('!')

expr = pyparsing.infixNotation( INTEGER,
    [("!", 1, pyparsing.opAssoc.LEFT),
     ("^", 2, pyparsing.opAssoc.RIGHT),
     #(SIGNOP, 1, pyparsing.opAssoc.RIGHT), Something wrong with this
     (MULTOP, 2, pyparsing.opAssoc.LEFT),
     (PLUSOP, 2, pyparsing.opAssoc.LEFT),],
     lpar=pyparsing.Suppress('m{'),
     rpar=pyparsing.Suppress('}')
    )
    
class MathEvaluationFilter():
    def Process(self, _, text):
        """
        Main method to process given text and return a string with all the Math blocks
        completed, without stripping away the surrounding spaces.
        """
        out_text = text

        for tokens, start, end in pyparsing.nestedExpr( 'm{', '}', expr).scanString(text):
            out_text = out_text.replace(text[start:end], str(self.eval_list(tokens.asList())[0]))
            
        return out_text
            
    
    def eval_list(self, input):
        """TODO decipher"""
        if any(isinstance(seg, list) for seg in input):
            for seg in input:
                if isinstance(seg, list):
                    output = self.eval_list(seg)
                    str_out = ''.join(str(x) for x in output)
                    evaluation = ast.literal_eval(str_out)
                    return [evaluation if x==seg else x for x in input]
        return input  