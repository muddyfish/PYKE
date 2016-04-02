
import lang_ast
from nodes import Node
import copy

class LeftMap(Node):
    char = "L"
    args = 0
    results = None
    contents = -1
    
    def __init__(self, node):
        self.node = node
        self.args = node.args
       
    @Node.test_func([5, 3], [[3,4,5,6,7]], "+")
    @Node.test_func([[1,2,3,4], 2], [[1,4,9,16]], "^")
    @Node.test_func([[1,0,"","hi"]], [[0,1,1,0]], "!")
    def func(self, *args):
        """for i in args[-1]:
    `node`(i, other_args)
Where other_args is the remaining arguments for the function.
These are taken from the stack. The same arguments are used for each map.
Returns the results of the map (extend mode)"""
        args = list(args)
        args = copy.deepcopy(args)
        reverse = True
        if isinstance(args[0], int):
            args[0] = list(range(args[0]))
        try:
            max_len = len(args[0])
        except TypeError:
            args = args[::-1]
            max_len = len(args[0])
            reverse = False
        argtype = type(args[0])
        for i, arg in enumerate(args):
            if i == 0: continue
            args[i] = [arg]*max_len
        results = []
        for i in zip(*args):
            if reverse: i = i[::-1]
            rtn = self.node(i)
            if len(rtn) == 1: rtn = rtn[0]
            results.append(rtn)
        if argtype is str:
            try:
                return "".join(results)
            except TypeError:
                return results
        return [argtype(results)]
    
    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.args)
        
    @classmethod
    def accepts(cls, code):
        if code[0] == cls.char:
            code, node = lang_ast.AST.add_node(code[1:])
            assert(node is not None)
            return code, cls(node)
        return None, None