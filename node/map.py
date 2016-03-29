
import lang_ast
from nodes import Node
import copy

class Map(Node):
    char = "m"
    args = 0
    results = None
    contents = 1000
    
    def __init__(self, node):
        self.node = node
        self.args = node.args
       
    @Node.test_func([[-4,2,3,4], 5], [[1,7,8,9]], "+")
    @Node.test_func([[1,0,"","hi"]], [[0,1,1,0]], "!")
    def func(self, *args):
        """for i in args[0]:
    `node`(i, other_args)
Where other_args is the remaining arguments for the function.
These are taken from the stack. The same arguments are used for each map.
Returns the results of the map (extend mode)"""
        args = list(args)
        args = copy.deepcopy(args)
        argtype = type(args[0])
        max_len = len(args[0])
        for i, arg in enumerate(args):
            if i == 0: continue
            args[i] = [arg]*max_len
        results = []
        for i in zip(*args):
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