#!/usr/bin/env python

from nodes import Node

class Dict(Node):
    char = "Y"
    args = 1
    results = 1
        
    @Node.test_func([[["test", 2], [2,3]]], [{"test":2,2:3}])
    def func(self, a:Node.sequence):
        """Turn a sequence into a dict"""
        return dict(a)
