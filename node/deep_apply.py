import lang_ast
from nodes import Node
import copy

class DeepApply(Node):
    char = "A"
    args = 1
    results = 1
    
    def __init__(self, node):
        self.node = node
    
    @Node.test_func([[[(0, 0), (0, 1)], [(1, 0), (1, 1)]]], [[[0, 1], [1, 2]]], "+")
    def func(self, seq: Node.sequence):
        """Deeply apply a node to a nD tree"""
        return [self.recurse(seq)]

    def recurse(self, seq):
        if isinstance(seq[0][0], Node.sequence):
            return [self.recurse(i) for i in seq]
        else:
            rtn = []
            for i in seq:
                try:
                    val = self.node(i)
                except AssertionError:
                    val = self.node([i])
                if len(val) > 1: rtn.append(val)
                else: rtn.extend(val)
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