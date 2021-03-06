#!/usr/bin/env python

from nodes import Node


class Negate(Node):
    char = "_"
    args = 1
    results = 1
    contents = 333333

    @Node.test_func([[3,2]], [[2,3]])
    def reverse(self, sequence: Node.indexable):
        """sequence[::-1]"""
        return [sequence[::-1]]
    
    @Node.test_func([7], [-7])
    def func(self, a: Node.number):
        """-a"""
        return -a
