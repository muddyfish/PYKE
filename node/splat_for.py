from node.for_loop import For
from node.splat import Splat
from nodes import Node


class SplatFor(Node):
    char = "XF"
    args = None
    results = None
    default_arg = 1
    
    def __init__(self, args: Node.NumericLiteral, ast:Node.EvalLiteral):
        self.args = args
        self.ast = ast
        if self.ast.nodes == []:
            self.ast.add_node("}")

    def func(self, *args):
        """For loop.
When finished, splat output"""
        looper = For(self.args, self.ast)
        looper.contents = False
        splatter = Splat()
        rtn = looper(args)
        return splatter(rtn)
