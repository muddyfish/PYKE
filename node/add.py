#!/usr/bin/env python

from nodes import Node

@Node.test("+", [1,2], [3])
@Node.test("+", [0,[1,2,3]], [[1,2,3,0]])
@Node.test("+", [[1,2,3],4], [[4,1,2,3]])
@Node.test("+", [[3,4],[1,2]], [[1,2,3,4]])
class Add(Node):
    """
    Takes two items from the stack and adds them
    """
    char = "+"
    args = 2
    results = 1
    
    def join_sequence(self, a:Node.sequence, b:Node.sequence):
        return[type(a)(list(a)+list(b))]
    
    def append_sequence(self, a:Node.sequence, b):
        return[type(a)(list(a)+[b])]
    
    def prepend_sequence(self, a, b:Node.sequence):
        return[type(b)([a]+list(b))]
    
    def func(self, a,b):
        return a+b