import lang_ast
from nodes import Node
import copy

class DeepApply(Node):
    char = "A"
    args = 1
    results = 1
    
    def __init__(self, node:Node.NodeSingle):
        self.node = node
    
    def prepare(self, stack):
        #print("IN_STACK", stack)
        if stack != [] and self.choose_function(stack) == self.splat_args:
            self.args = len(stack)
            self.results = None
        else:            
            args = 1
            results = 1
    
        
        
    @Node.test_func([[[(0, 0), (0, 1)], [(1, 0), (1, 1)]]], [[[0, 1], [1, 2]]], "+")
    @Node.prefer
    def func(self, seq: Node.sequence):
        """Deeply apply a node to a nD tree"""
        return [self.recurse(seq)]

    def recurse(self, seq):
        if isinstance(seq[0][0], Node.sequence):
            return [self.recurse(i) for i in seq]
        else:
            rtn = []
            for i in copy.deepcopy(seq):
                try:
                    val = self.node(i)
                except AssertionError:
                    val = self.node([i])
                if len(val) > 1: rtn.append(val)
                else: rtn.extend(val)
            return rtn
    
    @Node.test_func([30], ["30"], '"')
    @Node.is_func
    def splat_args(self, *args):
        """Splat a node with a static suffix and run it"""
        arg = str(args[-1])
        code, node = self.node.accepts(self.node.char+arg)
        #Warn if code empty?
        stack = list(args[:-1])
        node.prepare(stack[::-1])
        no_args = node.args
        stack, args = stack[no_args:], stack[:no_args]
        stack = node(args[::-1]) + stack
        return stack
    
    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.args)
        