#!/usr/bin/env python

from nodes import Node
from node.string_literal import StringLiteral 

class Split(Node):
    char = "c"
    args = 2
    results = 1
    
    @Node.test_func(["1 2 1", " "], [["1", "2", "1"]])
    @Node.test_func(["1,3,4", ","], [["1", "3", "4"]])
    def split(self, inp:str, split:str):
        """inp.split(`arg`)"""
        return [inp.split(split)]
    