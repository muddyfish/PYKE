#!/usr/bin/env python

from nodes import Node

class BitXOR(Node):
    args = 2
    results = 1
    char = ".^"
    
    @Node.test_func([4,5], [1])
    def func(self, a:int,b:int):
        """a^b"""
        return a^b

    @Node.test_func(["Test.", "Te"], [1])
    @Node.test_func(["Test.", "?"], [0])
    @Node.test_func(["Test.", "T"], [1])
    def startswith(self, string:str, suffix:str):
        """Does string start with suffix?"""
        return int(string.startswith(suffix))
    