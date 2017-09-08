import pyparsing, re, ast

integer = pyparsing.Word(pyparsing.nums)

expop = pyparsing.Literal('^')
signop = pyparsing.oneOf('+ -')
multop = pyparsing.oneOf('* /')
plusop = pyparsing.oneOf('+ -')
factop = pyparsing.Literal('!')

expr = pyparsing.infixNotation( integer,
    [("!", 1, pyparsing.opAssoc.LEFT),
     ("^", 2, pyparsing.opAssoc.RIGHT),
     (signop, 1, pyparsing.opAssoc.RIGHT),
     (multop, 2, pyparsing.opAssoc.LEFT),
     (plusop, 2, pyparsing.opAssoc.LEFT),],
     lpar=pyparsing.Suppress('m{'),
     rpar=pyparsing.Suppress('}')
    )
    
class MathEvaluationFilter():
    def Process(self, engine, text):
        out_text = text
        for tokens, start, end in pyparsing.nestedExpr( 'm{', '}', expr).scanString(text):
            out_text = out_text.replace(text[start:end], str(self.eval_list(tokens.asList())[0]))
        return out_text
            
    
    def eval_list(self, input):
        if any(isinstance(seg, list) for seg in input):
            for seg in input:
                if isinstance(seg, list):
                    output = self.eval_list(seg)
                    str_out = ''.join(str(x) for x in output)
                    evaluation = ast.literal_eval(str_out)
                    return [evaluation if x==seg else x for x in input]
        return input  