#!/usr/bin/env python

from nodes import Node

class FloorDiv(Node):
    char = "f"
    args = 2
    results = 1
    
    @Node.test_func([3,2], [1])
    @Node.test_func([6,-3], [-2])
    def func(self, a:Node.number,b:Node.number):
        """a/b. Rounds down, returns an int."""
        return a//b
    
    @Node.test_func(["test", "e"], [["t", "e", "st"]])
    def partition(self, string:str, sep:str):
        """Split the string at the first occurrence of sep,
return a 3-list containing the part before the separator,
the separator itself, and the part after the separator.
If the separator is not found,
return a 3-list containing the string itself,
followed by two empty strings."""
        return [list(string.partition(sep))]