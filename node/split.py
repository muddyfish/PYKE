#!/usr/bin/env python

from nodes import Node
from node.string_literal import StringLiteral 

class Split(Node):
    char = "c"
    args = 1
    results = 1
    default_arg = " "
    
    def __init__(self, string:Node.StringLiteral):
        self.string = string or Split.default_arg
    
    @Node.test_func(["1 2 1"], [["1", "2", "1"]])
    @Node.test_func(["1,3,4"], [["1", "3", "4"]], ",")
    def split(self, inp:str):
        """inp.split(`arg`)"""
        return [inp.split(self.string)]
    
    def __repr__(self):
        return "%s: %r"%(self.__class__.__name__, self.string)
    