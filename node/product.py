#!/usr/bin/env python

from nodes import Node

class Product(Node):
    char = "B"
    args = 1
    results = 1
    
    @Node.test_func([[1,2]], [2])
    @Node.test_func([[3,4]], [12])
    @Node.test_func([[3,4,2]], [24])
    def func(self, inp:Node.sequence):
        """return product of integer sequence"""
        current = 1
        for val in inp:
            current *= val
        return [current]