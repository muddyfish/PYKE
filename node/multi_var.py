
from nodes import Node

class MultiVar(Node):
    char = "'"
    args = 0
    results = None
    contents = -1
    
    def __init__(self, node_1: Node.NodeSingle, node_2: Node.NodeSingle):
        self.node_1 = node_1
        self.node_2 = node_2
        self.args = max([node_1.args, node_2.args])
        
    def prepare(self, stack):
        if len(stack) == 0:
            self.add_arg(stack)

    @Node.is_func
    def apply(self, *stack):
        self.node_2.prepare(stack)
        rtn = self.node_2(stack[:self.node_2.args])
        self.node_1.prepare(stack)
        rtn.extend(self.node_1(stack[:self.node_1.args]))
        return rtn
