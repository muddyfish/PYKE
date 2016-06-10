from nodes import Node
from fractions import gcd

class LCM(Node):
    char = ".L"
    args = 2
    results = 1
    contents = ()

    def prepare(self, stack):
        if len(stack) == 0:
            self.add_arg(stack)
        if isinstance(stack[0], Node.sequence):
            self.args = 1

    @Node.test_func([3, 7], [21])
    @Node.test_func([6, 14], [42])
    def lcm(self, a: int, b: int):
        """Return the lowest common multiple of 2 numbers"""
        return a * b // gcd(a, b)
    
    @Node.test_func([[30, 24, 12]], [120])
    def lcm_seq(self, a: Node.sequence):
        """Return the lowest common multiple of n numbers"""
        while len(a) != 1:
            a.append(self.lcm(a.pop(), a.pop()))
        return a