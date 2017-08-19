import lang_ast
from nodes import Node


class Eval(Node):
    char = ""
    args = 0
    results = None
    ignore = True
    
    def __init__(self, ast):
        self.ast = ast
        
    def func(self, *args):
        return self.ast
    
    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.args)
        
    @classmethod
    def accepts(cls, code, accept=False):
        if not accept:
            return None, None
        ast = lang_ast.AST()
        code = ast.setup(code)
        return code, cls(ast)
