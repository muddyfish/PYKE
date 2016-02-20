import lang_ast
from nodes import Node
from node.numeric_literal import NumericLiteral 

class Eval(Node):
    char = ""
    args = 0
    results = None
    
    def __init__(self, ast):
        self.ast = ast
        
    def func(self, *args):
        return self.ast
    
    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.args)
        
    @classmethod
    def accepts(cls, code, accept = False):
        if not accept: return None, None
        ast = lang_ast.AST()
        code = ast.setup(code)
        return code, cls(ast)