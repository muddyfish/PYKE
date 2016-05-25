import lang_ast
from nodes import Node
from node.numeric_literal import NumericLiteral
import copy

class Repeat(Node):
    char = "V"
    args = None
    results = 1
    
    def __init__(self, ast:Node.EvalLiteral):
        self.ast = ast
        if self.ast.nodes == []:
            self.ast.add_node("\n")

    def prepare(self, stack):
        self.args = len(stack)
            
    def func(self, *stack):
        """For i in range(repeats):
    stack = eval_literal(stack)
return stack"""
        stack = copy.deepcopy(list(stack))
        repeats = stack.pop()
        for i in range(repeats):
            stack = self.ast.run(list(stack))
        return stack