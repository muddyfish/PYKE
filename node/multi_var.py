
from nodes import Node

class MultiVar(Node):
    char = "'"
    args = 0
    results = None
    contents = -1
    
    def __init__(self, node_1: Node.NodeSingle, node_2: Node.NodeSingle):
        self.node_1 = node_1
        self.node_2 = node_2
        
    def prepare(self, stack):
        self.node_1.prepare(stack)
        self.node_2.prepare(stack)
        self.args = max([self.node_1.args,self.node_2.args])

    @Node.is_func
    def apply(self, *stack):
        try:
            rtn = self.node_2(stack[:self.node_2.args])
            rtn.extend(self.node_1(stack[:self.node_1.args]))
            return rtn
        except Exception:
            rtn = self.node_2(stack[:self.node_2.args][::-1])
            rtn.extend(self.node_1(stack[:self.node_1.args][::-1]))
            return rtn
