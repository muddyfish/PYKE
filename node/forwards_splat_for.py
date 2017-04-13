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
        self.ast.empty = self.ast.nodes == []
        if self.ast.empty:
            self.ast.add_node("}")
        self.looper = For(self.args, self.ast)
        self.looper.contents = False

    def prepare(self, stack):
        self.looper.prepare(stack)
        self.args = self.looper.args

    def func(self, *args):
        """For loop.
When finished, splat output forwards"""
        rtn = self.looper(args[::-1])
        if len(rtn) == 1:
            rtn = rtn[0]
        return list(rtn)[::-1]
