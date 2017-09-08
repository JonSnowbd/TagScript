import pyparsing, re, ast, functools

INTEGER = pyparsing.Word(pyparsing.nums)

EXPOP = pyparsing.Literal('^')
SIGNOP = pyparsing.oneOf('+ -')
MULTOP = pyparsing.oneOf('* /')
PLUSOP = pyparsing.oneOf('+ -')
FACTOP = pyparsing.Literal('!')

expr = pyparsing.infixNotation( INTEGER,
    [("!", 1, pyparsing.opAssoc.LEFT),
     ("^", 2, pyparsing.opAssoc.RIGHT),
     (MULTOP, 2, pyparsing.opAssoc.LEFT),
     (PLUSOP, 2, pyparsing.opAssoc.LEFT),],
     lpar=pyparsing.Suppress('m{'),
     rpar=pyparsing.Suppress('}')
    )
    
OP_DICT = {'+': {'REGEX': re.compile("(\d+\s*)\+(\s*\d+)"), 
                 'func_name': 'addf'},
           '-': {'REGEX': re.compile("(\d+\s*)\-(\s*\d+)"), 
                 'func_name': 'subf'},
           '^': {'REGEX': re.compile("(\d+\s*)\^(\s*\d+)"), 
                 'func_name': 'powf'},
           '!': {'REGEX': re.compile("(\d+\s*)\!"), 
                 'func_name': 'facf'},
           '*': {'REGEX': re.compile("(\d+\s*)\*(\s*\d+)"), 
                 'func_name': 'mulf'},
           '/': {'REGEX': re.compile("(\d+\s*)\/(\s*\d+)"), 
                 'func_name': 'divf'}
           }
                   
REGEX = re.compile("[mM]{(.+[^}])}")
class MathEvaluationFilter():
    def Process(self, engine, text):
        """Processes provided text, returning text but with math blocks solved"""
        out_text = text
        while REGEX.search(text):
            for tokens, start, end in pyparsing.nestedExpr( 'm{', '}', expr).scanString(text):
                out_text = out_text.replace(text[start:end], str(self.eval_list(tokens.asList())[0]))
            text = out_text
        return text

    def eval_list(self, input):
        if any(isinstance(seg, list) for seg in input):
            out_dict = input
            for seg in input:
                if isinstance(seg, list):
                    output = self.eval_list(seg)
                    str_out = ''.join(str(x) for x in output)
                    for op in OP_DICT:
                        if op in str(str_out):
                            handler = getattr(self, OP_DICT[op]['func_name'], lambda: None)
                            str_out = handler(str_out)
                    out_dict = [str_out if x==seg else x for x in out_dict]
            return out_dict
        return input         

    # Various AST hacks :(

    def addf(self, input):
        while OP_DICT['+']['REGEX'].search(str(input)):
            matches = OP_DICT['+']['REGEX'].match(str(input))
            input = input.replace(input[matches.start():matches.end()], str(functools.reduce(lambda a,b:a+b,[int(matches.group(1)), int(matches.group(2))])))
        return input
        
    def subf(self, input):
        while OP_DICT['-']['REGEX'].search(str(input)):
            matches = OP_DICT['-']['REGEX'].match(str(input))
            input = input.replace(input[matches.start():matches.end()], str(functools.reduce(lambda a,b:a-b,[int(matches.group(1)), int(matches.group(2))])))
        return input
        
    def powf(self, input):
        while OP_DICT["^"]["REGEX"].search(str(input)):
            matches = OP_DICT['^']['REGEX'].match(str(input))
            input = input.replace(input[matches.start():matches.end()], str(functools.reduce(lambda a,b:a*b,[int(matches.group(1))]*int(matches.group(2)))))
        return input
        
    def facf(self, input):
        while OP_DICT['!']['REGEX'].search(str(input)):
            matches = OP_DICT['!']['REGEX'].match(str(input))
            input = input.replace(input[matches.start():matches.end()], str(functools.reduce(lambda a,b:a*b,range(1,int(matches.group(1))+1))))
        return input
        
    def mulf(self, input):
        while OP_DICT['*']['REGEX'].search(str(input)):
            matches = OP_DICT['*']['REGEX'].match(str(input))
            input = input.replace(input[matches.start():matches.end()], str(functools.reduce(lambda a,b:a*b,[int(matches.group(1)), int(matches.group(2))])))
        return input
        
    def divf(self, input):
        while OP_DICT['/']['REGEX'].search(str(input)):
            matches = OP_DICT['/']['REGEX'].match(str(input))
            input = input.replace(input[matches.start():matches.end()], str(functools.reduce(lambda a,b:a/b,[int(matches.group(1)), int(matches.group(2))])))
        return input