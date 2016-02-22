import lang_ast
from nodes import Node
from node.numeric_literal import NumericLiteral 

class First_N(Node):
    char = ".f"
    args = 2
    results = 1
    
    def __init__(self, ast: Node.EvalLiteral):
        self.ast = ast
        
    def prepare(self, stack):
        if len(stack) < 2:
            self.args = 1
    
    def first_n_start(self, count: int, start: int):
        results = []
        i = start
        while len(results) != count:
            rtn = self.ast.run([i])
            if len(rtn) != 0 and rtn[-1]:
                results.append(i)
            i+=1
        return [results]
    
    def first_n(self, count: int):
        return self.first_n_start(count, 1)
    
    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.args)