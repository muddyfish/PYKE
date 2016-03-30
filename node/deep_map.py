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
       
    def func(self, *args):
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