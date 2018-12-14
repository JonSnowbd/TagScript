from .. import engine
from . import Block
from typing import Optional

import ast
import operator as op

# supported operators
operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
             ast.USub: op.neg}

# Safeguard for 100**100**100
def power(a, b):
    if any(abs(n) > 100 for n in [a, b]):
        raise ValueError((a,b))
    return op.pow(a, b)
operators[ast.Pow] = power

def eval_expr(expr):
    """
    >>> eval_expr('2^6')
    4
    >>> eval_expr('2**6')
    64
    >>> eval_expr('1 + 2*3**(4^5) / (6 + -7)')
    -5.0
    """
    return eval_(ast.parse(expr, mode='eval').body)

def eval_(node):
    if isinstance(node, ast.Num): # <number>
        return node.n
    elif isinstance(node, ast.BinOp): # <left> <operator> <right>
        return operators[type(node.op)](eval_(node.left), eval_(node.right))
    elif isinstance(node, ast.UnaryOp): # <operator> <operand> e.g., -1
        return operators[type(node.op)](eval_(node.operand))
    else:
        raise TypeError(node)

class MathBlock(Block):
    def will_accept(self, ctx : engine.Interpreter.Context) -> bool:
        dec = ctx.verb.declaration.lower()
        return any([dec == "math", dec == "m", dec == "+"])

    def process(self, ctx : engine.Interpreter.Context) -> Optional[str]:
        try: 
            result = eval_expr(ctx.verb.payload.strip(" "))
            ctx.handled = True
            return str(result)
        except:
            return None