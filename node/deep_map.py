import lang_ast
from nodes import Node
import copy

class DeepMap(Node):
    char = "M"
    args = 0
    results = None
    
    def __init__(self, node):
        self.node = node
        self.args = node.args
    
    @Node.test_func([[[0,1,2,3],[4,5,6,7]]], [[[0, 2, 4, 6], [8, 10, 12, 14]]], "}")
    def func(self, *args):
        """Deeply map an operation across a nD tree.
Takes a list or tuple with a varying depth.
Returns a list with the same depth all round with the function applied."""
        seq, *args = copy.deepcopy(args)
        assert(isinstance(seq,Node.sequence))
        return [self.recurse(seq, args)]
        

    def recurse(self, seq, args):
        rtn = []
        for i in seq:
            if isinstance(i, Node.sequence):
                rtn.append(self.recurse(i, args))
            else:
                rtn.append(self.run(i, args))
        return rtn
    
    def run(self, obj, args):
        rtn = self.node([obj]+args)
        if len(rtn) == 1: rtn = rtn[0]
        return rtn
    
    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.args)
        
    @classmethod
    def accepts(cls, code):
        if code[0] == cls.char:
            code, node = lang_ast.AST.add_node(code[1:])
            assert(node is not None)
            return code, cls(node)
        return None, None