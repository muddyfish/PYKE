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
    
    @Node.test_func(["134", 1], [["134"]])
    @Node.test_func(["1234", 2], [["12", "34"]])
    @Node.test_func(["1234", 3], [["1", "2", "34"]])
    @Node.test_func([[4,8,15,16,23,42], 5], [[[4],[8],[15],[16],[23,42]]])
    def chunk(self, inp:Node.indexable, num:int):
        """Return inp seperated into num groups"""
        rtn = []
        last = 0
        size = len(inp)//num
        for i in range(size, len(inp), size):
            rtn.append(inp[last:i])
            last = i
        if len(rtn) != num:
            rtn.append(inp[last:])
        else:
            rtn[-1] += inp[last:]
        if len(rtn):
            if isinstance(inp, str):
                rtn[-1] = "".join(rtn[-1])
            else:
                rtn[-1] = type(inp)(rtn[-1])
        return [rtn]