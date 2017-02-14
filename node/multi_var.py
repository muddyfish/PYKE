
from nodes import Node


class MultiVar(Node):
    char = "'"
    args = 0
    results = None
    contents = 100
    
    def __init__(self, node_1: Node.NodeSingle, node_2: Node.NodeSingle):
        self.node_1 = node_1
        self.node_2 = node_2
        
    def prepare(self, stack):
        self.node_1.prepare(stack)
        self.node_2.prepare(stack)
        self.args = max([self.node_1.args,self.node_2.args])

    @Node.test_func([1, 5], [2, 4], "-h")
    @Node.test_func([5], [6, 4], "th")
    @Node.test_func(["hello"], ["h", "ello"], "th")
    @Node.is_func
    def apply(self, *stack):
        """With the current stack, run the next 2 nodes with that stack.
Pops `n` items from the stack where `n` is the greatest number of elements required.
When a different number of args are taken by the nodes, the one that takes fewest consumes
from closest to start of stack first towards the top of stack"""
        try:
            rtn = self.node_2(stack[:self.node_2.args])
            rtn.extend(self.node_1(stack[:self.node_1.args]))
            return rtn
        except Exception:
            rtn = self.node_2(stack[:self.node_2.args][::-1])
            rtn.extend(self.node_1(stack[:self.node_1.args][::-1]))
            return rtn
