#!/usr/bin/env python

from nodes import Node

class Str(Node):
    char = "`"
    args = 1
    results = 1
    
    @Node.test_func([[3,2]], ["[3, 2]"])
    @Node.test_func([17], ["17"])
    @Node.test_func([4.2], ["4.2"])
    @Node.test_func(["Hi"], ["Hi"])
    def func(self, a):
        """str(a)"""
        return [str(a)]