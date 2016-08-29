import lang_ast
from nodes import Node
import copy

class Repeat(Node):
    char = "V"
    args = None

    def __init__(self, ast:Node.EvalLiteral):
        self.ast = ast
        if self.ast.nodes == []:
            self.ast.add_node("\n")

    def prepare(self, stack):
        self.args = max(1, len(stack))

    @Node.test_func([2, 3], [256], "X")
    @Node.test_func([5], [1,1,1,1,1], "1")
    def func(self, *stack):
        """For i in range(repeats):
    stack = eval_literal(stack)
return stack"""
        stack = copy.deepcopy(list(stack))
        repeats = stack.pop()
        try:
            old = repeats
            repeats = len(repeats)
        except TypeError: pass
        else:
            stack.append(old)
        for i in range(repeats):
            stack = self.ast.run(list(stack))
        self.results = len(stack)
        return stack