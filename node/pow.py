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
    