from node.for_loop import For
from nodes import Node


class ForwardsSplatFor(Node):
    char = " F"
    args = None
    results = None
    default_arg = 1
    
    def __init__(self, args: Node.NumericLiteral, ast:Node.EvalLiteral):
        self.args = args
        self.ast = ast
        if self.ast.nodes == []:
            self.ast.add_node("}")

    def func(self, *args):
        looper = For(self.args, self.ast)
        looper.contents = False
        rtn = looper(args)
        if len(rtn) == 1:
            rtn = rtn[0]
        return list(rtn)[::-1]
