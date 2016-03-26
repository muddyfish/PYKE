import lang_ast
from nodes import Node
from node.numeric_literal import NumericLiteral 

class Eval(Node):
    char = "E"
    args = 1
    results = None
        
    def prepare(self, stack):
        self.args = max(len(stack), 1)
        
    def func(self, *args):
        """Takes entire stack.
Evals first item as Pyke code.
Returns resulting stack onto the stack"""
        ast = lang_ast.AST()
        ast.setup(args[0])
        return [ast.run(list(args[1:]))]
    
    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.args)
        