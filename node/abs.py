#!/usr/bin/env python

from nodes import Node

class Abs(Node):
    char = ".a"
    args = 2
    results = 1

    @Node.test_func([1,2], [1])
    @Node.test_func([5,2], [3])
    @Node.test_func([-1,2], [3])
    def abs_diff(self, a:Node.number, b:Node.number):
        """Returns the absolute difference between 2 numbers"""
        return abs(a-b)
    