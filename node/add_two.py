#!/usr/bin/env python

from nodes import Node

@Node.test("O", [2], [4])
@Node.test("O", [[1,2,3]], [[1,2]])
class Pop(Node):
    char = "O"
    args = 1
    results = 1
    
    def add_two(self, inp: Node.number):
        """inp+2"""
        return inp+2
    
    def rm_end(self, inp: Node.indexable):
        """inp[:-1]"""
        return [inp[:-1]]