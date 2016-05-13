from nodes import Node

class While(Node):
    char = "W"
    args = None
    results = None
    contents = 1
    
    def __init__(self, ast:Node.EvalLiteral):
        self.ast = ast
        
    def prepare(self, stack):
        self.args = len(stack)
    
    @Node.test_func([0], [5], "hD 5N")
    def func(self, *stack):
        """Takes stack, returns stack.
while not continue:
    stack = run_ast(stack)
    continue = pop(stack)
return stack"""
        cont = True
        max_num = 1000
        while cont and max_num:
            stack = self.ast.run(list(stack))[::-1]
            cont = stack.pop()
            max_num -= 1
        return stack
    
    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.args)