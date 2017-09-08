import pyparsing, re, functools

integer = pyparsing.Word(pyparsing.nums)

expop = pyparsing.Literal('^')
signop = pyparsing.oneOf('+ -')
multop = pyparsing.oneOf('* /')
plusop = pyparsing.oneOf('+ -')
factop = pyparsing.Literal('!')

expr = pyparsing.infixNotation( integer,
    [("!", 1, pyparsing.opAssoc.LEFT),
     ("^", 2, pyparsing.opAssoc.RIGHT),
     (multop, 2, pyparsing.opAssoc.LEFT),
     (plusop, 2, pyparsing.opAssoc.LEFT),],
     lpar=pyparsing.Suppress('m{'),
     rpar=pyparsing.Suppress('}')
    )
    
op_dict = {'+': {'REGEX': re.compile("(\d+\s*)\+(\s*\d+)"), 
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
                    for op in op_dict:
                        if op in str(str_out):
                            handler = getattr(self, op_dict[op]['func_name'], lambda: None)
                            str_out = handler(str_out)
                    out_dict = [str_out if x==seg else x for x in out_dict]
            return out_dict
        return input         
        
    def addf(self, input):
        while op_dict['+']['REGEX'].match(str(input)):
            matches = op_dict['+']['REGEX'].match(str(input))
            input = functools.reduce(lambda a,b:a+b,[int(matches.group(1)), int(matches.group(2))])
        return input
        
    def subf(self, input):
        while op_dict['-']['REGEX'].match(str(input)):
            matches = op_dict['-']['REGEX'].match(str(input))
            input = functools.reduce(lambda a,b:a-b,[int(matches.group(1)), int(matches.group(2))])
        return input
        
    def powf(self, input):
        while op_dict["^"]["REGEX"].match(str(input)):
            matches = op_dict['^']['REGEX'].match(str(input))
            input = functools.reduce(lambda a,b:a*b,[int(matches.group(1))]*int(matches.group(2)))
        return input
        
    def facf(self, input):
        while op_dict['!']['REGEX'].match(str(input)):
            matches = op_dict['!']['REGEX'].match(str(input))
            input = functools.reduce(lambda a,b:a*b,range(1,int(matches.group(1))+1))
        return input
        
    def mulf(self, input):
        while op_dict['*']['REGEX'].match(str(input)):
            matches = op_dict['*']['REGEX'].match(str(input))
            input = functools.reduce(lambda a,b:a*b,[int(matches.group(1)), int(matches.group(2))])
        return input
        
    def divf(self, input):
        while op_dict['/']['REGEX'].match(str(input)):
            matches = op_dict['/']['REGEX'].match(str(input))
            input = functools.reduce(lambda a,b:a/b,[int(matches.group(1)), int(matches.group(2))])
        return input
