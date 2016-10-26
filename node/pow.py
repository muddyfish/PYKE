#!/usr/bin/env python

from nodes import Node

class Pow(Node):
    """
    Takes two items from the stack and raises a^b
    """
    char = "^"
    args = 2
    results = 1
    

    @Node.test_func([3,2], [9])
    @Node.test_func([2,-2], [0.25])
    def func(self, a: Node.number, b: Node.number):
        """a**b"""
        return a**b
    
    @Node.test_func(["Test.", "."], [1])
    @Node.test_func(["Test.", "?"], [0])
    @Node.test_func(["Test.", "t."], [1])
    def endswith(self, string:str, suffix:str):
        """Does string end with suffix?"""
        return int(string.endswith(suffix))
    
    @Node.test_func([[1, 2, 3, 4, 5], [10, 10, 4, 62, 7]], [22167])
    @Node.test_func([[4, 2], [5, 10]], [42])
    @Node.test_func([[3, 0, 7], [5, 1, 10]], [37])
    def mixed_base(self, inp:Node.sequence, bases:Node.sequence):
        """Convert from a mixed base number to an integer"""
        prod = 1
        for val in bases:
            prod *= val
        cur = 0
        for e, i in enumerate(inp):
            prod //= bases[e]
            cur += i*prod
        return cur

    def lpad(self, string: str, amount: int):
        return string.ljust(amount)