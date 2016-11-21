import copy

from nodes import Node


class For(Node):
    char = "F"
    args = None
    results = None
    default_arg = 1
    contents = 1
    
    def __init__(self, args: Node.NumericLiteral, ast:Node.EvalLiteral):
        self.args = args
        self.ast = ast
        if self.ast.nodes == []:
            self.ast.add_node("\n")
        
    @Node.test_func([[1,5]], [[2,10]], "}")
    @Node.test_func([[1,5], 2], [[4,12]], "2}+")
    @Node.test_func([3, 2], [[0,2,4]], "2*")
    @Node.test_func(["tesT"], ["1110"], "$`")
    def func(self, *args):
        """Constant arg - how many items off the stack to take, default 1
arg1 - object to iterate over (if int, range(arg1))
Returns a list of lists to the stack"""
        args = list(args)
        args = copy.deepcopy(args)
        is_int = isinstance(args[0], int)
        if is_int:
            args[0] = range(args[0])
        max_len = len(args[0])
        for i, arg in enumerate(args[1:]):
            args[i+1] = [arg]*max_len
        results = []
        for i in zip(*args):
            rtn = self.ast.run(list(i))
            if len(rtn) == 1:
                rtn = rtn[0]
            results.append(rtn)
        if isinstance(args[0], str) and all(isinstance(i, str) for i in results) and self.contents:
            return "".join(results)
        return [results]