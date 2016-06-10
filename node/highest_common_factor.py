from nodes import Node
from fractions import gcd

class HCF(Node):
    char = ".H"
    args = 2
    results = 1
    contents = {}

    def prepare(self, stack):
        if len(stack) == 0:
            self.add_arg(stack)
        if isinstance(stack[0], Node.sequence):
            self.args = 1
            
    @Node.test_func([8,4], [4])
    @Node.test_func([15,24], [3])
    def hcf(self, a: int, b: int):
        """Return the highest common factor of 2 numbers"""
        return gcd(a,b)
    
    @Node.test_func([[30, 24, 12]], [6])
    def hcf_seq(self, a: Node.sequence):
        """Return the highest common factor of n numbers"""
        while len(a) != 1:
            a.append(self.hcf(a.pop(), a.pop()))
        return a